from agents.intelligence_agent import IntelligenceAgent
import time

def main():
    print("=== Starting Autonomous Multi-Agent System ===")

    # Initialize the brain
    brain = IntelligenceAgent()

    # Define initial context
    context = {
        'target_url': 'https://malubeach.wordpress.com',
        'scraped_data_file': 'links.json',
        'search_query': 'site:malubeach.wordpress.com'
    }

    # Run the autonomous loop
    start_time = time.time()
    brain.run(context)
    duration = time.time() - start_time

    print(f"\n=== System Cycle Complete in {duration:.2f} seconds ===")

    # Output generated artifacts
    robots_content = brain.generate_robots_txt()
    print("\n[Artifact Generated] robots.txt Preview:")
    print("-" * 40)
    print(robots_content)
    print("-" * 40)

if __name__ == "__main__":
    main()
