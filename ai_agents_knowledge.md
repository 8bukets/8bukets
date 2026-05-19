# AI Agents Knowledge Repository

Synthesized from Google Innovation & AI Blog

## [Accelerating Gemma 4: faster inference with multi-token prediction drafters](https://blog.google/innovation-and-ai/technology/developers-tools/multi-token-prediction-gemma-4/)

### Definitions
- **Why speculative decoding?**: The technical reality is that standard LLM inference is memory-bandwidth bound, creating a significant latency bottleneck. The processor spends the majority of its time moving billions of parameters from VRAM to the compute units just to generate a single token. This leads to under-utilized compute and high latency, especially on consumer-grade hardware. Speculative decoding decouples token generation from verification. By pairing a heavy target model (e.g., Gemma 4 31B) with a lightweight drafter (the MTP model), we can utilize idle compute to “predict” several future tokens at once with the drafter in less time than it takes for the target model to process just one token. The target model then verifies all of these suggested tokens in parallel.
- **How speculative decoding works**: Standard large language models generate text autoregressively, producing exactly one token at a time. While effective, this process dedicates the same amount of computation to predicting an obvious continuation (like predicting “words” after “Actions speak louder than…”) as it does to solving a complex logic puzzle. MTP mitigates this inefficiency through speculative decoding, a technique introduced by Google researchers in Fast Inference from Transformers via Speculative Decoding . If the target model agrees with the draft, it accepts the entire sequence in a single forward pass —and even generates an additional token of its own in the process. This means your application can output the full drafted sequence plus one token in the time it usually takes to generate a single one.

### Use Cases
- **Unlocking faster AI from the edge to the workstation**: For developers, inference speed is often the primary bottleneck for production deployment. Whether you are building coding assistants, autonomous agents that require rapid multi-step planning, or responsive mobile applications running entirely on-device, every millisecond matters. By pairing a Gemma 4 model with its corresponding drafter, developers can achieve: Improved responsiveness: Drastically reduce latency for near real-time chat, immersive voice applications and agentic workflows. Supercharged local development: Run our 26B MoE and 31B Dense models on personal computers and consumer GPUs with unprecedented speed, powering seamless, complex offline coding and agentic workflows. Enhanced on-device performance: Maximize the utility of our E2B and E4B models on edge devices by generating outputs faster, which in turn preserves valuable battery life. Zero quality degradation: Because the primary Gemma 4 model retains the final verification, you get identical frontier-class reasoning and accuracy, just delivered significantly faster.

### Google Cloud Tools
- Gemini
- Gemma
- LiteRT
- Hugging Face
- Kaggle
- vLLM
- MLX

---

## [Models & research](https://blog.google/innovation-and-ai/models-and-research/)

### Google Cloud Tools
- Gemini
- Google Flow

---

## [Gemini API File Search is now multimodal: build efficient, verifiable RAG](https://blog.google/innovation-and-ai/technology/developers-tools/expanded-gemini-api-file-search-multimodal-rag/)

### Google Cloud Tools
- Gemini
- Gemma
- Kaggle

---

## [Google Labs](https://blog.google/innovation-and-ai/models-and-research/google-labs/)

### Definitions
- **Introducing “vibe design” with Stitch**: Stitch is evolving into an AI-native platform that allows anyone to create, iterate, and collaborate on high-fidelity UI.

### Google Cloud Tools
- Gemini

---

## [Join the new AI Agents Vibe Coding Course from Google and Kaggle](https://blog.google/innovation-and-ai/technology/developers-tools/kaggle-genai-intensive-course-vibe-coding-june-2026/)

### Definitions
- **General summary**: Google and Kaggle are bringing back their free five-day AI Agents Intensive course from June 15–19, 2026. You will learn to build production-ready AI agents using natural language workflows and hands-on coding projects. Register on the website now to secure your spot and complete the final capstone project.
- **Basic explainer**: Google and Kaggle are bringing back their free five-day AI course this June. You'll learn how to build powerful AI agents using "vibe coding," which lets you create programs just by using natural language. The course includes hands-on projects to help you turn your own ideas into real systems. You can sign up on their website to get started.

### Benefits
- **Bullet points**: Google and Kaggle are hosting a free AI Agents Vibe Coding course this June. You’ll learn to build powerful AI agents using natural language as your main tool. The five-day program includes expert speakers, updated lessons and a hands-on capstone project. You’ll master how to connect tools and APIs to create highly effective AI systems. Sign up on their website to start building your own production-ready AI agents.

### Google Cloud Tools
- Gemini
- Kaggle

---

## [AlphaEvolve, 1 year later: Impact on science, technology](https://blog.google/innovation-and-ai/infrastructure-and-cloud/google-cloud/alphaevolve-updates/)

### Google Cloud Tools
- Gemini

---

## [Gemini Models](https://blog.google/innovation-and-ai/models-and-research/gemini-models/)

### Google Cloud Tools
- Gemini

---

## [Gemini Embedding 2 is now generally available](https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-embedding-2-generally-available/)

### Google Cloud Tools
- Gemini

---

## [Google DeepMind](https://blog.google/innovation-and-ai/models-and-research/google-deepmind/)

### Google Cloud Tools
- Gemini
- Kaggle

---

## [Google Research](https://blog.google/innovation-and-ai/models-and-research/google-research/)

### Google Cloud Tools
- Gemini

---

## [Quantum computing](https://blog.google/innovation-and-ai/models-and-research/quantum-computing/)

### Google Cloud Tools
- Gemini

---

## [Gemini App](https://blog.google/innovation-and-ai/products/gemini-app/)

### Google Cloud Tools
- Gemini

---

## [How to make a study guide with Gemini using handwritten notes](https://blog.google/innovation-and-ai/products/gemini-app/digitize-notes-gemini-study-guide/)

### Google Cloud Tools
- Gemini

---

## [Gemini 3.1 Flash Live: Making audio AI more natural and reliable](https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-3-1-flash-live/)

### Definitions
- **General summary**: Gemini 3.1 Flash Live is Google's highest-quality audio model, designed for natural and reliable real-time dialogue. Developers can access it through the Gemini Live API in Google AI Studio, while enterprises can use it for customer experience. Everyone can experience it via Search Live and Gemini Live, which now supports over 200 countries.

### Benefits
- **Bullet points**: "Gemini 3.1 Flash Live" is here, making AI audio sound more natural and reliable. This new audio model is faster and better at understanding tone for natural conversations. Developers can use it to build voice agents that handle complex tasks more reliably. Gemini Live and Search Live now offer more helpful responses in many languages. All audio from 3.1 Flash Live is watermarked to help prevent the spread of misinformation.

### Google Cloud Tools
- Gemini
- SynthID

---

## [Deep Research Max: a step change for autonomous research agents](https://blog.google/innovation-and-ai/models-and-research/gemini-models/next-generation-gemini-deep-research/)

### Definitions
- **Basic explainer**: Google just released two new AI research agents that can dig through massive amounts of data to write professional reports. One version is built for speed, while the other, called Deep Research Max, handles complex, deep-dive projects. These tools can even create their own charts and connect to your private files to find specific answers. It’s a huge upgrade that helps people get expert-level analysis done much faster than before.
- **Choose a research configuration that fits your workflow**: Building upon our initial release of Gemini Deep Research, we’re introducing two distinct agents designed to match your needs ranging from direct user assistance to large-scale, offline research processes: Deep Research: Optimized for speed and efficiency, this new agent replaces our preview release from December and delivers significantly reduced latency and cost at higher quality levels. It is the ideal agent for research experiences integrated directly into interactive user surfaces where lower latency is desired. Deep Research Max: Designed for maximum comprehensiveness and highest-quality synthesis, Max leverages extended test-time compute to iteratively reason, search and refine the final report. It is the perfect engine for asynchronous, background workflows such as a nightly cron job triggering the generation of exhaustive due diligence reports for an analyst team by morning.

### Use Cases
- **Drive real-world results with expert-grade analysis**: Deep Research Max delivers highly comprehensive reports, rigorous factuality and expert-grade analysis cheaper and more efficiently than ever before. Compared to our December release, Deep Research Max consults significantly more sources and identifies critical nuances the older release frequently overlooked. We have also focused on teaching Deep Research to consult a diverse array of sources and carefully weighing conflicting evidence against each other. The result is a nuanced report that draws from authoritative sources like SEC filings and open-access peer-reviewed journals, lays out information well and transforms dense technical data into actionable, stakeholder-ready formats.

### Benefits
- **Bullet points**: Google’s "Deep Research Max" article introduces powerful new autonomous agents for advanced data analysis. Choose between the fast Deep Research agent or the comprehensive Deep Research Max model. These agents now securely connect to your private data using the Model Context Protocol. The system creates professional charts and infographics to help you visualize complex research findings. You can now guide the agent's research plan to ensure you get exactly what's needed.
- **Unlock proprietary data and rich native visuals**: Deep Research can now search the web, arbitrary remote MCPs, file uploads and connected file stores — or any subset of them — introducing capabilities designed to handle the complex, gated data universes that professionals rely on daily. Model Context Protocol (MCP) support: You can now seamlessly connect Deep Research to your custom data and specialized professional data streams (such as financial or market data providers) securely via MCP. Deep Research supports arbitrary tool definitions which transforms it from a web searcher into an autonomous agent capable of navigating any specialized data repositories. Native charts and infographics: A first for Deep Research in the Gemini API, our agent no longer just creates text; it natively generates high-quality charts and infographics in-line with HTML or Nano Banana , dynamically visualizing complex data sets to enrich analytical reports.
- **Take advantage of proven Google scale performance**: When you build with the Deep Research agent, you are tapping into the same autonomous research infrastructure that powers research capabilities within some of Google’s most popular products like Gemini App , NotebookLM , Google Search and Google Finance .

### Google Cloud Tools
- Gemini models
- Gemini
- Model Context Protocol
- MCP
- Interactions API
- Nano Banana

---

## [Gemini Models](https://blog.google/innovation-and-ai/models-and-research/gemini-models/rss/)

### Google Cloud Tools
- Gemini
- Gemma
- Vertex AI
- Kaggle
- Nano Banana

---

## [Innovation & AI](https://blog.google/innovation-and-ai/)

### Google Cloud Tools
- Infrastructure & cloud
- Gemini

---

## [Infrastructure & Cloud](https://blog.google/innovation-and-ai/infrastructure-and-cloud/)

### Google Cloud Tools
- 7 highlights from Google Cloud Next ‘26
- Google Cloud Next ‘26
- Gemini

---

## [Global Network](https://blog.google/innovation-and-ai/infrastructure-and-cloud/global-network/)

### Google Cloud Tools
- Gemini

---

## [Google Cloud](https://blog.google/innovation-and-ai/infrastructure-and-cloud/google-cloud/)

### Google Cloud Tools
- 7 highlights from Google Cloud Next ‘26
- Google Cloud Next ‘26
- Gemini

---

## [Google Threat Intelligence Group reports on AI threat trends.](https://blog.google/innovation-and-ai/infrastructure-and-cloud/google-cloud/google-threat-intelligence-group-report/)

### Google Cloud Tools
- Gemini

---

## [Products](https://blog.google/innovation-and-ai/products/)

### Google Cloud Tools
- Gemini

---

## [NotebookLM](https://blog.google/innovation-and-ai/products/notebooklm/)

### Google Cloud Tools
- Gemini

---

## [Technology](https://blog.google/innovation-and-ai/technology/)

### Google Cloud Tools
- Gemini
- Gemma

---

## [AI](https://blog.google/innovation-and-ai/technology/ai/)

### Benefits
- **AI Impact Summit 2026: How we’re partnering to make AI work for everyone**: An overview of Google’s new global partnerships and funding announcements at the AI Impact Summit in India.

### Google Cloud Tools
- Gemini

---

## [The latest AI news we announced in April 2026](https://blog.google/innovation-and-ai/technology/ai/google-ai-updates-april-2026/)

### Definitions
- **General summary**: Google’s April updates focused on the "agentic era," introducing the Gemini Enterprise Agent Platform, eighth-generation chips, and the powerful Gemma 4 open model. You can now access new tools like Google Vids for free video creation, Deep Research Max for data analysis, and a personalized coding tutor in Colab. Check out the new AI Agents Vibe Coding course on Kaggle to start building software today.
- **Basic explainer**: Google announced a bunch of new AI tools in April to help people work, study and create more easily. They launched features like a free video generator, a personal coding tutor and advanced research assistants. These updates aim to make AI more helpful for everything from school projects to professional business tasks. Google is also using this tech to improve healthcare and language translation for everyone.

### Benefits
- **Bullet points**: Check out "The latest AI news we announced in April" for Google's newest tech updates. Google Cloud introduced powerful new tools and chips to help businesses build AI agents. You can now create professional videos for free using the new Google Vids suite. New coding tools like Learn Mode in Colab act as your personal programming tutor. Google is using AI to improve healthcare access and help students with test prep.

### Google Cloud Tools
- Gemini
- Gemma
- Kaggle

---

## [Developer tools](https://blog.google/innovation-and-ai/technology/developers-tools/)

### Google Cloud Tools
- Gemini
- Kaggle

---

## [Health](https://blog.google/innovation-and-ai/technology/health/)

### Google Cloud Tools
- Gemini

---

## [Safety & Security](https://blog.google/innovation-and-ai/technology/safety-security/)

### Google Cloud Tools
- Gemini

---

## [Evolving expectations of what’s possible](https://blog.google/innovation-and-ai/technology/safety-security/evolving-expectations-of-whats-possible/)

### Google Cloud Tools
- Gemini

---

## [We’re launching the Google DeepMind Accelerator program in Asia Pacific to tackle environmental risks.](https://blog.google/innovation-and-ai/models-and-research/google-deepmind/accelerator-ai-for-the-planet/)

### Google Cloud Tools
- Gemini

---

## [Cloud Next ‘26: Momentum and innovation at Google scale](https://blog.google/innovation-and-ai/infrastructure-and-cloud/google-cloud/cloud-next-2026-sundar-pichai/)

### Definitions
- **Basic explainer**: Google is growing its cloud business fast by helping companies build and manage thousands of AI agents. They’re launching new, powerful computer chips to handle all this extra work and keep systems secure from hackers. Google also uses its own AI tools to write code and fix security bugs much faster than before. These updates help businesses get more done with less effort.
- **3. Introducing our eighth-generation TPUs**: In the era of AI agents, infrastructure needs to evolve to take on the most demanding AI workloads. This year, we’re bringing the eighth generation of our Tensor Processing Units with a dual chip approach: TPU 8t , optimized for training, scales up to 9,600 TPUs and 2 petabytes of shared, high-bandwidth memory in a single superpod. It achieves three times the processing power of Ironwood and delivers up to 2x more performance/watt. TPU 8i , optimized for inference, connects 1,152 TPUs in a single pod, dramatically reducing latency, with 3x more on-chip SRAM, to deliver the massive throughput and low latency needed to concurrently run millions of agents cost-effectively. We’ll offer these to Cloud customers as a core part of our selection of compute processors, along with a portfolio of NVIDIA GPU instances. Read more in our blog post .

### Google Cloud Tools
- Gemini

---

## [7 highlights from Google Cloud Next ‘26](https://blog.google/innovation-and-ai/infrastructure-and-cloud/google-cloud/google-cloud-next-26-recap/)

### Definitions
- **Basic explainer**: Google is moving into the "agentic era," where AI acts as a partner that can actually do work for you. They launched new tools that let anyone build these AI helpers without needing to know how to code. They also upgraded their massive computer chips and data systems to make sure these agents run faster and stay secure. Big companies are already using this tech to handle everything from customer orders to complex research.

### Google Cloud Tools
- Gemini
- Nano Banana

---

## [How Google Does It: An inside look at cybersecurity](https://blog.google/innovation-and-ai/infrastructure-and-cloud/google-cloud/how-google-does-it-security-series/)

### Google Cloud Tools
- Gemini

---

## [Google Cloud Next ‘26](https://blog.google/innovation-and-ai/infrastructure-and-cloud/google-cloud/next-2026/)

### Google Cloud Tools
- Gemini

---

## [Google Cloud](https://blog.google/innovation-and-ai/infrastructure-and-cloud/google-cloud/rss/)

### Google Cloud Tools
- Gemini
- Kaggle

---

## [Measuring progress toward AGI: A cognitive framework](https://blog.google/innovation-and-ai/models-and-research/google-deepmind/measuring-agi-cognitive-framework/)

### Definitions
- **General summary**: Google DeepMind wants to help measure the progress of Artificial General Intelligence (AGI) using cognitive science. Their new paper, "Measuring Progress Toward AGI: A Cognitive Taxonomy," presents a framework for understanding AI systems' cognitive capabilities. You can participate by designing evaluations for key cognitive abilities in their Kaggle hackathon for a chance to win from a prize pool of $200,000.

### Google Cloud Tools
- Gemini
- Kaggle

---

## [Google DeepMind](https://blog.google/innovation-and-ai/models-and-research/google-deepmind/rss/)

### Google Cloud Tools
- Gemini
- Kaggle
- Nano Banana

---

## [Google Labs](https://blog.google/innovation-and-ai/models-and-research/google-labs/rss/)

### Google Cloud Tools
- Gemini
- Nano Banana
- Google Flow

---

## [Introducing “vibe design” with Stitch](https://blog.google/innovation-and-ai/models-and-research/google-labs/stitch-ai-ui-design/)

### Definitions
- **General summary**: Stitch now uses AI to help you create high-fidelity UI designs from natural language. The new AI-native canvas lets you explore ideas, add images, text, or code, and provides a design agent to track your progress. Use voice commands for real-time design critiques and export designs to developer tools.

### Google Cloud Tools
- Gemini
- MCP
- Google Flow

---

## [Google Research](https://blog.google/innovation-and-ai/models-and-research/google-research/rss/)

### Google Cloud Tools
- Gemini
- Nano Banana

---

## [Research](https://blog.google/innovation-and-ai/technology/research/)

### Google Cloud Tools
- Gemini

---

## [Building superconducting and neutral atom quantum computers](https://blog.google/innovation-and-ai/technology/research/neutral-atom-quantum-computers/)

### Google Cloud Tools
- Gemini

---

## [Quantum frontiers may be closer than they appear](https://blog.google/innovation-and-ai/technology/safety-security/cryptography-migration-timeline/)

### Google Cloud Tools
- Gemini

---

## [Blackstone and Google to develop TPU cloud](https://blog.google/innovation-and-ai/infrastructure-and-cloud/google-cloud/blackstone-tpu-cloud/)

### Google Cloud Tools
- Gemini

---

## [Introducing Gemini Omni](https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-omni/)

### Use Cases
- **Edit your videos through conversation**: Gemini Omni gives you an easier way to edit video — with natural language. Every instruction builds on the last. Your characters stay consistent, the physics hold up and the scene remembers what came before. Transform the world around you. Change specific things, or change everything. Your video becomes the starting point for something you never could have filmed yourself.
- **Bring ideas to life, grounded in Gemini’s world knowledge**: Gemini Omni doesn't just build scenes that look real, it reasons about what should happen next. It combines an intuitive understanding of physics with Gemini's knowledge of history, science and cultural context, bridging the gap from photorealism to meaningful storytelling. Create visuals with more accurate physics. Omni has an improved intuitive understanding of forces like gravity, kinetic energy and fluid dynamics, allowing you to create more realistic scenes.
- **Create videos from any combination of inputs**: Reference anything. Omni turns any reference — image, text, video or audio — into a single, cohesive output. While only voice references will be supported for audio to start, we’ll roll out other types of audio inputs soon.
- **Create videos with your own digital avatar**: We're committed to developing AI responsibly and we have clear policies to protect users from harm and governing the use of our AI tools. To start, you can create videos with your own voice by using Avatars , which create a digital version of yourself so you can generate videos that look and sound like you. Beyond the avatar feature, in terms of editing videos to change audio and speech, we are still working to test this and better understand how we can bring this capability to users responsibly. All videos created with Omni include our imperceptible SynthID digital watermark. You can easily verify that videos were generated with Gemini Omni through the Gemini app, Gemini in Chrome and Google Search. You can find out more about how we're expanding our content transparency and verification tools to help you understand how content was created and edited across the web in our blog post .

### Google Cloud Tools
- Gemini
- Kaggle
- Nano Banana
- Google Flow
- YouTube Shorts
- YouTube Create App
- SynthID
- Avatars

---

## [Simulate real-world places with Project Genie and Street View](https://blog.google/innovation-and-ai/models-and-research/google-deepmind/project-genie-expands/)

### Google Cloud Tools
- Gemini
- Google Flow

---

## [The Gemini app becomes more agentic, delivering proactive, 24/7 help](https://blog.google/innovation-and-ai/products/gemini-app/next-evolution-gemini-app/)

### Google Cloud Tools
- Gemini
- MCP

---

## [Making it easier to understand how content was created and edited](https://blog.google/innovation-and-ai/products/identifying-ai-generated-media-online/)

### Google Cloud Tools
- Gemini
- SynthID

---

## [I/O 2026: Welcome to the agentic Gemini era](https://blog.google/innovation-and-ai/sundar-pichai-io-2026/)

### Google Cloud Tools
- Infrastructure supporting innovation at scale
- Gemini
- MCP
- Nano Banana
- Google Flow
- YouTube Shorts
- SynthID

---

## [Bring any idea to life: Google AI Studio at I/O 2026](https://blog.google/innovation-and-ai/technology/developers-tools/google-ai-studio-io-2026/)

### Google Cloud Tools
- Gemini
- Gemma
- Nano Banana

---

## [Introducing Managed Agents in the Gemini API](https://blog.google/innovation-and-ai/technology/developers-tools/managed-agents-gemini-api/)

### Google Cloud Tools
- Get access to Google's agent infrastructure
- Reason, plan and call tools using the harness
- Execute code and manage files in an isolated Linux sandbox
- Browse the web to fetch and process live data
- Gemini
- Gemma
- Interactions API

---


All the best - https://markposition.wordpress.com
