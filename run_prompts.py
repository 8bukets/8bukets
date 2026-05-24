import argparse
import os
import re
import asyncio
import json
import random
import logging
from google import genai
from google.genai import types

# Setup logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(levelname)s] %(message)s")

# Creative defaults for placeholders
CREATIVE_DEFAULTS = {
    "NICHE": "Artificial Intelligence in Sustainable Agriculture",
    "TOPIC": "The impact of autonomous drones on crop yield optimization",
    "DESCRIBE YOUR AUDIENCE — e.g., \"tech-savvy 25-40 year olds who build with AI tools\"": "Tech-savvy agronomists and climate-conscious investors aged 30-50",
    "SPECIFIC TONE — e.g., \"direct, punchy, slightly irreverent. No corporate speak.\"": "Direct, visionary, and slightly provocative. No corporate jargon.",
    "WORD COUNT — e.g., \"2,500-3,000 words\"": "500-800 words",
    "YOUR TOPIC": "Building autonomous AI agents for daily life",
    "YOUR AUDIENCE": "Software engineers looking to automate their workflows",
    "PASTE YOUR CONTENT": "AI agents are moving from research labs to production environments. In the next 5 years, every knowledge worker will have a personal swarm of agents handling scheduling, research, and coding tasks.",
    "DESCRIBE AUDIENCE": "Busy founders and indie hackers",
    "PLATFORM": "Twitter/X",
    "HOW OFTEN — e.g., \"daily\" or \"5x per week\"": "3x per week",
    "e.g., \"threads, single posts, articles, polls, engagement posts\"": "threads, contrarian takes, and behind-the-scenes building",
    "PASTE BLOG POST": "The rise of generative AI has fundamentally changed how we write code. Instead of remembering syntax, developers now focus on architecture and problem-solving, acting more as reviewers of AI-generated solutions.",
    "TARGET KEYWORD": "autonomous ai agents",
    "PASTE ARTICLE": "An autonomous AI agent is a system capable of executing complex workflows without human intervention. By chaining thought processes and utilizing tools, these agents can solve multi-step problems.",
    "WHO": "Acme Corp, a mid-sized logistics company",
    "WHAT THEY WERE STRUGGLING WITH": "High fuel costs and inefficient routing leading to late deliveries",
    "WHAT WAS IMPLEMENTED": "An AI-driven predictive routing algorithm",
    "SPECIFIC OUTCOMES — use numbers": "Reduced fuel costs by 22% and improved on-time delivery from 81% to 98%",
    "LENGTH — e.g., \"10-minute\"": "3-minute",
    "TONE — e.g., \"conversational like talking to a smart friend, not like a lecture\"": "fast-paced, high-energy, and highly actionable",
    "DESCRIBE YOURSELF — role, expertise, achievements": "Ex-founder, AI researcher, built 3 products to $10k MRR",
    "WHO DO YOU WANT TO ATTRACT": "Ambitious builders and early-stage founders",
    "e.g., \"confident but not arrogant, slightly witty\"": "authoritative but approachable, showing proof of work",
    "CHARACTER LIMIT": "160",
    "YOUR PRODUCT/COMPANY": "NeuroTask (An AI to-do list that does the tasks for you)",
    "LIST COMPETITORS": "Motion, Todoist, Asana",
    "AXIS 1": "Price (Low to High)",
    "AXIS 2": "Automation Level (Manual to fully autonomous)",
    "DESCRIBE YOUR IDEA": "A marketplace for renting out idle GPU compute from consumer gaming PCs",
    "WHO IT IS FOR": "Gamers with high-end rigs and AI researchers needing cheap compute",
    "HOW IT MAKES MONEY": "20% transaction fee on all rentals",
    "IDEA / MVP / LAUNCHED": "MVP phase",
    "PRODUCT/SERVICE": "AI Code Review Assistant",
    "DESCRIPTION": "A GitHub app that reviews PRs, finds bugs, and suggests performance improvements using LLMs",
    "CURRENT PRICE": "$0 during beta",
    "WHAT COMPETITORS CHARGE": "$20-50/developer/month",
    "COST PER UNIT/USER": "Approx $5/month in LLM API costs",
    "PROBLEM": "B2B sales teams spend 60% of their time researching leads instead of selling",
    "SOLUTION": "An AI agent that autonomously researches, scores, and drafts personalized outreach for prospects",
    "MARKET": "$12B Sales Tech Market",
    "REVENUE MODEL": "SaaS subscription: $199/user/month",
    "METRICS": "10 pilot customers, $2k MRR, saving reps 15 hours/week",
    "TEAM BACKGROUND": "Ex-Salesforce engineers and a former VP of Sales",
    "HOW MUCH AND WHAT FOR": "Raising $2M Seed to build out the GTM team and scale engineering",
    "PASTE RAW DATA — metrics, notes, observations, whatever you have": "Revenue: $45k (+10% WoW). Churn: 2% (down from 3%). Released the new dashboard feature on Tuesday. Had 3 critical bugs reported, all hotfixed by Thursday. Marketing spend was $5k with a CAC of $50.",
    "COMPANY/PRODUCT/PROJECT": "Launch of a new AI-powered mobile email client",
    "PROVIDE RELEVANT CONTEXT": "Entering a crowded market dominated by Gmail and Apple Mail, but focusing specifically on power users who get 200+ emails a day.",
    "POTENTIAL PARTNER": "A popular productivity newsletter with 100k subscribers",
    "YOUR COMPANY/ROLE": "Founder of an AI calendar app",
    "THEIR COMPANY/ROLE": "Editor-in-chief of 'The Daily Planner'",
    "MUTUAL BENEFIT": "We provide a 6-month free premium subscription to their readers; we get high-intent user acquisition",
    "SPECIFIC ASK": "A dedicated sponsorship slot or interview feature next month",
    "PRODUCT": "NeuroTask AI To-Do List",
    "WHERE THE PRODUCT IS NOW": "Live with 1,000 active users. Core task management works, but AI automation is basic.",
    "LIST THEM": "Mobile app is buggy, AI takes too long to generate subtasks, no Google Calendar sync",
    "TEAM SIZE/CONSTRAINTS": "2 full-stack engineers, 1 designer. Limited budget for external APIs.",
    "LENGTH": "45 minutes",
    "WHAT DECISION OR OUTCOME": "Whether to pivot from B2C to B2B enterprise sales",
    "FEATURE DESCRIPTION": "User Authentication System with OAuth and Magic Links",
    "YOUR STACK — e.g., \"Next.js, TypeScript, Supabase, Tailwind\"": "Next.js, TypeScript, Supabase",
    "BRIEF DESCRIPTION": "A greenfield Next.js 14 App Router project",
    "REQUIREMENT 1": "Support Email/Password login",
    "REQUIREMENT 2": "Support Google and GitHub OAuth",
    "REQUIREMENT 3": "Implement session persistence and middleware route protection",
    "CONSTRAINT — e.g., \"Must work on mobile\"": "Must be highly secure against CSRF and XSS",
    "CONSTRAINT — e.g., \"Under 200ms response time\"": "Minimal external dependencies",
    "PASTE CODE": "def calculate_fibonacci(n):\n    if n <= 0:\n        return 0\n    elif n == 1:\n        return 1\n    else:\n        return calculate_fibonacci(n-1) + calculate_fibonacci(n-2)",
    "APPLICATION DESCRIPTION": "A multi-tenant SaaS for managing freelance invoices",
    "DATA REQUIREMENT 1": "Users can belong to multiple organizations (workspaces)",
    "DATA REQUIREMENT 2": "Invoices have multiple line items and track payment status",
    "DATA REQUIREMENT 3": "Clients need to be tracked per organization",
    "DATABASE — e.g., \"PostgreSQL\"": "PostgreSQL",
    "FEATURE/APPLICATION": "A smart home IoT temperature logging service",
    "LANGUAGE/FRAMEWORK": "Node.js with Express",
    "PASTE ERROR": "TypeError: Cannot read properties of undefined (reading 'map')",
    "WHAT SHOULD HAPPEN": "The component should render a list of user profiles",
    "WHAT ACTUALLY HAPPENS": "The app crashes on load when the API request is delayed",
    "HOW TO TRIGGER THE BUG": "Throttling the network to 3G in Chrome DevTools causes the crash",
    "FUNCTION/COMPONENT/MODULE": "A utility function that parses and formats dates from various string inputs (e.g., 'YYYY-MM-DD', 'MM/DD/YYYY') into a standard ISO format",
    "TESTING FRAMEWORK — e.g., \"Jest\", \"pytest\"": "pytest",
    "PROJECT/API/LIBRARY": "A python library 'image-optimizer' that batch resizes and compresses JPEGs and PNGs using multi-threading",
    "PASTE CODE OR API SPEC": "class ImageOptimizer:\n  def __init__(self, quality=85):\n    self.quality = quality\n  def optimize_folder(self, input_dir, output_dir):\n    # implementation",
    "APPLICATION": "A containerized Python FastAPI microservice",
    "YOUR STACK": "Python, Docker, Pytest",
    "WHERE — e.g., \"Vercel\", \"AWS\", \"Railway\"": "AWS ECS",
    "PLATFORM — e.g., \"GitHub\"": "GitHub",
    "WHAT THE CODE DOES AND WHERE IT RUNS": "A React component that renders a large table of 5000 rows. It runs in the browser.",
    "MARKET/INDUSTRY": "The emerging market of AI-powered legal document review tools",
    "INDUSTRY": "Remote Work Technology",
    "PASTE DATA": "User cohort 1 (Jan): 1000 signups, 20% D1 retention, 5% D30. Cohort 2 (Feb): 1200 signups, 25% D1, 8% D30. Feature X adoption: 15% overall, but 40% among users retained >30 days.",
    "RESEARCH QUESTION": "Why users cancel their subscription within the first 14 days",
    "DECISION TO MAKE": "Which cloud provider to migrate our infrastructure to",
    "LIST YOUR OPTIONS": "AWS, Google Cloud (GCP), Microsoft Azure",
    "CRITERION 1": "Cost effectiveness",
    "CRITERION 2": "Developer experience and tooling",
    "CRITERION 3": "AI/Machine Learning managed services",
    "CRITERION 4": "Vendor lock-in risk",
    "1-5": "4",
    "PROJECT/DECISION/VENTURE": "Launching a physical hardware wallet for cryptocurrency",
    "ROLE": "Senior Backend Engineer (Go/gRPC)",
    "JUNIOR/MID/SENIOR": "Senior",
    "LIST SKILLS": "Go, gRPC, microservices architecture, Kubernetes, PostgreSQL",
    "DESCRIBE YOUR TEAM": "Fast-moving, highly autonomous, remote-first team dealing with high-throughput financial data",
    "PASTE LEGAL DOCUMENT": "The Receiving Party shall not use any Confidential Information of the Disclosing Party for any purpose other than evaluating a potential business relationship between the parties. The Receiving Party shall restrict dissemination of Confidential Information to only those employees who have a 'need to know' and are bound by confidentiality obligations at least as restrictive as those contained herein.",
    "COMPETITOR NAME/URL": "stripe.com/blog",
    "LIST YOUR TASKS": "1. Review PR #42. 2. Draft Q3 roadmap. 3. Fix production bug in payment webhook. 4. Reply to investor emails. 5. Write weekly team update. 6. Brainstorm new marketing copy.",
    "YOUR MAIN GOAL": "Ensure system stability and close the funding round",
    "HOW MANY HOURS": "8",
    "PASTE EMAIL SUBJECTS AND SENDERS — or full emails": "1. Urgent: Payment gateway failing for EU customers (From: DevOps lead) 2. Introduction: John from VC Firm (From: Advisor) 3. Your weekly newsletter digest 4. Feature request: Dark mode (From: Customer Support) 5. PTO Request for next Friday (From: Junior Dev)",
    "PASTE NOTES OR TRANSCRIPT": "Attendees: Alice, Bob, Charlie. Discussed the Q3 marketing budget. Alice proposed increasing ad spend by 20%. Bob argued we should focus on SEO. Decision: We will increase ad spend by 10% as a test and allocate the rest to hiring a freelance SEO writer. Action item: Alice to adjust the ad campaigns by Friday. Charlie to post the job description for the SEO writer by Wednesday.",
    "SKILL I WANT TO LEARN": "Rust Programming Language",
    "BEGINNER / INTERMEDIATE / ADVANCED": "Beginner to Rust, but Senior in Python/JavaScript",
    "HOURS PER WEEK": "10",
    "HOW LONG — e.g., \"3 months\"": "2 months",
    "hands-on projects, not lectures": "Project-based learning building CLI tools and a small web server",
    "PROCESS": "Onboarding a new B2B Enterprise Client",
    "WHO PERFORMS THIS PROCESS AND WHY": "The Customer Success Manager, to ensure the client is set up correctly and experiences value within 14 days",
    "PASTE YOUR INCOME, EXPENSES, OR FINANCIAL SUMMARY": "Monthly Net Income: $6000. Rent: $2000. Groceries: $600. Dining out: $400. Car payment: $350. Student loans: $300. Subscriptions: $100. Investing: $500. Remaining cash: $1750.",
    "LIST YOUR DESIRED HABITS": "1. Daily 30-minute coding practice before work. 2. Meditate for 10 minutes at lunch.",
    "DESCRIBE YOUR TYPICAL DAY": "Wake up at 7am, check phone, work 9-5 remotely, feel tired at 5pm, watch Netflix until 11pm.",
    "WHAT STOPS YOU": "Lack of energy after work, getting distracted by phone in the morning.",
    "CUE": "I pour my morning coffee",
    "HABIT": "sit at my desk and open my IDE",
    "LOCATION": "my home office",
    "WHAT YOU ARE NEGOTIATING": "A 20% salary increase during my annual performance review",
    "WHAT I WANT": "$120k base salary (up from $100k)",
    "WHAT THEY PROBABLY WANT": "To keep me happy but cap increases at 5% due to budget constraints",
    "MY BACKUP PLAN": "I have an offer from another company for $115k",
    "HIGH / MEDIUM / LOW": "High (I want to stay long-term)",
    "YOUR DECISION": "Whether to accept a promotion to Engineering Manager or stay as a Senior Individual Contributor",
    "DESCRIBE": "Engineering Manager. Higher salary ceiling, more influence, but means giving up daily coding and dealing with people problems.",
    "Option B: [DESCRIBE]": "Option B: Stay Senior IC. Keep coding, less stress, but less influence on overall technical direction and potentially capping out my career growth at this company."
}

def parse_prompts(filepath="PROMPTS.md"):
    if not os.path.exists(filepath):
        logging.error(f"{filepath} not found.")
        return []

    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()

    parts = re.split(r"^### Prompt ", content, flags=re.MULTILINE)

    prompts = []
    for part in parts[1:]:
        lines = part.strip().split("\n")
        title_line = lines[0]
        match = re.match(r"(\d+)\s*[—\-]\s*(.*)", title_line)
        if match:
            prompt_num = match.group(1)
            prompt_title = match.group(2).strip()
            prompt_text = "\n".join(lines[1:]).strip()
            prompts.append({
                "num": prompt_num,
                "title": prompt_title,
                "text": prompt_text
            })
    return prompts

def replace_placeholders(prompt_text):
    filled_prompt = prompt_text
    placeholders = re.findall(r"\[(.*?)\]", prompt_text)

    # Handle the duplicate placeholder edge case in Prompt 50 creatively
    option_b_handled = False

    for p in placeholders:
        replacement = CREATIVE_DEFAULTS.get(p)
        if replacement:
            filled_prompt = filled_prompt.replace(f"[{p}]", replacement, 1) # replace 1 by 1
        else:
            fallback = "Random Value"
            for k, v in CREATIVE_DEFAULTS.items():
                if k.lower() in p.lower() or p.lower() in k.lower():
                    fallback = v
                    break

            # Specialized edge case handling
            if p == "DESCRIBE" and option_b_handled:
                fallback = CREATIVE_DEFAULTS.get("Option B: [DESCRIBE]")
            elif p == "DESCRIBE":
                option_b_handled = True # next one will be B

            if fallback == "Random Value":
                 if "TOPIC" in p: fallback = "AI in Agriculture"
                 elif "NICHE" in p: fallback = "Tech Startups"
                 elif "AUDIENCE" in p: fallback = "Developers"
                 elif "B-ROLL" in p: fallback = "Shot of typing on keyboard"

            filled_prompt = filled_prompt.replace(f"[{p}]", fallback, 1)

    return filled_prompt

async def run_prompt_async(client, prompt_data, output_dir, max_retries=3):
    prompt_num = prompt_data["num"]
    prompt_title = prompt_data["title"]
    raw_text = prompt_data["text"]

    filled_text = replace_placeholders(raw_text)

    filename = os.path.join(output_dir, f"prompt_{prompt_num}_{prompt_title.replace(' ', '_').replace('/', '_')}.md")

    # Creative Skip: Resume capability
    if os.path.exists(filename):
        logging.info(f"⏭️ Skipping Prompt {prompt_num}: File already exists.")
        return True

    logging.info(f"Running Prompt {prompt_num}: {prompt_title}...")

    for attempt in range(max_retries):
        try:
            response = await client.aio.models.generate_content(
                model='gemini-2.5-flash',
                contents=filled_text,
            )

            output = f"# Prompt {prompt_num}: {prompt_title}\n\n"
            output += f"## Original Prompt (Filled)\n```text\n{filled_text}\n```\n\n"
            output += f"## AI Response\n\n{response.text}\n"

            with open(filename, "w", encoding="utf-8") as f:
                f.write(output)

            logging.info(f"✅ Saved results for Prompt {prompt_num} to {filename}")
            return True
        except Exception as e:
            error_str = str(e)
            if "429" in error_str and "RESOURCE_EXHAUSTED" in error_str:
                if "retry in" in error_str:
                    match = re.search(r"retry in (\d+\.\d+)s", error_str)
                    wait_time = float(match.group(1)) + 1.0 if match else 35.0
                    logging.warning(f"⚠️ Rate limited on Prompt {prompt_num}. Retrying in {wait_time:.1f}s...")
                    await asyncio.sleep(wait_time)
                else:
                    # Likely daily limit exhausted
                    logging.error(f"❌ Daily limit exhausted on Prompt {prompt_num}. Cannot retry today.")
                    return False
            else:
                logging.error(f"❌ Failed to run Prompt {prompt_num}: {e}")
                return False

    return False

async def main():
    parser = argparse.ArgumentParser(description="CLI tool to run AI Prompts.")
    parser.add_argument("--all", action="store_true", help="Run all prompts")
    parser.add_argument("--prompt", type=int, help="Run a specific prompt by number (1-50)")
    parser.add_argument("--outdir", default="results/prompts", help="Directory to save results")
    args = parser.parse_args()

    api_key = os.environ.get("GEMINI_API_KEY")
    if not api_key:
        logging.warning("GEMINI_API_KEY environment variable not set. Using a mock/dry-run mode.")
        mock_mode = True
    else:
        client = genai.Client(api_key=api_key)
        mock_mode = False

    prompts = parse_prompts()
    if not prompts:
        return

    os.makedirs(args.outdir, exist_ok=True)

    to_run = []
    if args.all:
        to_run = prompts
    elif args.prompt:
        to_run = [p for p in prompts if int(p["num"]) == args.prompt]
        if not to_run:
            logging.error(f"Prompt {args.prompt} not found.")
            return
    else:
        logging.info("Please specify --all or --prompt <num>. Run with -h for help.")
        return

    logging.info(f"Preparing to run {len(to_run)} prompts...")

    if mock_mode:
        for p in to_run:
            filename = os.path.join(args.outdir, f"prompt_{p['num']}_{p['title'].replace(' ', '_').replace('/', '_')}.md")
            if os.path.exists(filename):
                 logging.info(f"⏭️ Skipping Mock Prompt {p['num']}: File already exists.")
                 continue
            filled = replace_placeholders(p['text'])
            with open(filename, "w", encoding="utf-8") as f:
                f.write(f"# MOCK RUN - Prompt {p['num']}\n\n{filled}\n\n[MOCK RESPONSE]")
            logging.info(f"✅ Mock saved to {filename}")
        return

    # Creative Batching for limits (10 RPM allowed usually, so we batch by 3 and delay heavily if needed)
    batch_size = 3
    for i in range(0, len(to_run), batch_size):
        batch = to_run[i:i+batch_size]
        tasks = [run_prompt_async(client, p, args.outdir) for p in batch]
        results = await asyncio.gather(*tasks)

        # If any returned False due to daily limit, break the whole run gracefully
        if False in results:
            logging.error("Stopping execution due to unrecoverable rate limits (Daily Free Tier Quota Exhausted).")
            break

        if i + batch_size < len(to_run):
            logging.info("Batch complete. Waiting 10 seconds to respect RPM limits...")
            await asyncio.sleep(10)

    logging.info("Run finished (or paused due to daily limits)!")

if __name__ == "__main__":
    asyncio.run(main())
