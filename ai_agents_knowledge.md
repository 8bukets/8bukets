# What are AI Agents?

Scraped from [https://cloud.google.com/discover/what-are-ai-agents](https://cloud.google.com/discover/what-are-ai-agents)

## What is an AI agent?

Last Updated: 04/02/2026

AI agents are software systems that use AI to pursue goals and complete tasks on behalf of users. They show reasoning, planning, and memory and have a level of autonomy to make decisions, learn, and adapt.

Their capabilities are made possible in large part by the multimodal capacity of generative AI and AI foundation models. AI agents can process multimodal information like text, voice, video, audio, code, and more simultaneously; can converse, reason, learn, and make decisions. They can learn over time and facilitate transactions and business processes. Agents can work with other agents to coordinate and perform more complex workflows.

## Key features of an AI agent

As explained above, while the key features of an AI agent are reasoning and acting (as described in ReAct Framework ) more features have evolved over time.

- Reasoning: This core cognitive process involves using logic and available information to draw conclusions, make inferences, and solve problems. AI agents with strong reasoning capabilities can analyze data, identify patterns, and make informed decisions based on evidence and context.

- Acting : The ability to take action or perform tasks based on decisions, plans, or external input is crucial for AI agents to interact with their environment and achieve goals. This can include physical actions in the case of embodied AI, or digital actions like sending messages, updating data, or triggering other processes.

- Observing : Gathering information about the environment or situation through perception or sensing is essential for AI agents to understand their context and make informed decisions. This can involve various forms of perception, such as computer vision, natural language processing, or sensor data analysis.

- Planning : Developing a strategic plan to achieve goals is a key aspect of intelligent behavior. AI agents with planning capabilities can identify the necessary steps, evaluate potential actions, and choose the best course of action based on available information and desired outcomes. This often involves anticipating future states and considering potential obstacles.

- Collaborating : Working effectively with others, whether humans or other AI agents, to achieve a common goal is increasingly important in complex and dynamic environments. Collaboration requires communication, coordination, and the ability to understand and respect the perspectives of others.

- Self-refining : The capacity for self-improvement and adaptation is a hallmark of advanced AI systems. AI agents with self-refining capabilities can learn from experience, adjust their behavior based on feedback, and continuously enhance their performance and capabilities over time. This can involve machine learning techniques, optimization algorithms, or other forms of self-modification.

## What is the difference between AI agents, AI assistants, and bots?

AI assistants are AI agents designed as applications or products to collaborate directly with users and perform tasks by understanding and responding to natural human language and inputs. They can reason and take action on the users' behalf with their supervision.

AI assistants are often embedded in the product being used. A key characteristic is the interaction between the assistant and user through the different steps of the task. The assistant responds to requests or prompts from the user, and can recommend actions but decision-making is done by the user.


 | AI agent | AI assistant | Bot ﻿
Purpose | Autonomously and proactively perform tasks | Assisting users with tasks | Automating simple tasks or conversations
Capabilities | Can perform complex, multi-step actions; learns and adapts; can make decisions independently | Responds to requests or prompts; provides information and completes simple tasks; can recommend actions but the user makes decisions | Follows pre-defined rules; limited learning; basic interactions
Interaction | Proactive; goal-oriented | Reactive; responds to user requests | Reactive; responds to triggers or commands

## Key differences

- Autonomy : AI agents have the highest degree of autonomy, able to operate and make decisions independently to achieve a goal. AI assistants are less autonomous, requiring user input and direction. Bots are the least autonomous, typically following pre-programmed rules.

- Complexity : AI agents are designed to handle complex tasks and workflows, while AI assistants and bots are better suited for simpler tasks and interactions.

- Learning : AI agents often employ machine learning to adapt and improve their performance over time. AI assistants may have some learning capabilities, while bots typically have limited or no learning.

## How do AI agents work?

Every agent defines its role, personality, and communication style, including specific instructions and descriptions of available tools.

- Persona : A well defined persona allows an agent to maintain a consistent character and behave in a manner appropriate to its assigned role, evolving as the agent gains experience and interacts with its environment.

- Memory : The agent is equipped in general with short term, long term, consensus, and episodic memory. Short term memory for immediate interactions, long-term memory for historical data and conversations, episodic memory for past interactions, and consensus memory for shared information among agents. The agent can maintain context, learn from experiences, and improve performance by recalling past interactions and adapting to new situations.

- Tools : Tools are functions or external resources that an agent can utilize to interact with its environment and enhance its capabilities. They allow agents to perform complex tasks by accessing information, manipulating data, or controlling external systems, and can be categorized based on their user interface, including physical, graphical, and program-based interfaces. Tool learning involves teaching agents how to effectively use these tools by understanding their functionalities and the context in which they should be applied.

- Model : Large language models (LLMs) serve as the foundation for building AI agents, providing them with the ability to understand, reason, and act. LLMs act as the "brain" of an agent, enabling them to process and generate language, while other components facilitate reason and action.

## What are the types of agents in AI?

AI agents can be categorized in various ways based on their capabilities, roles, and environments. Here are some key categories of agents:

There are different definitions of agent types and agent categories.

## Based on interaction

One way to categorize agents is by how they interact with users. Some agents engage in direct conversation, while others operate in the background, performing tasks without direct user input:

- Interactive partners (also known as, surface agents): Assisting us with tasks like customer service, healthcare, education, and scientific discovery, providing personalized and intelligent support. Conversational agents include Q&A, chit chat, and world knowledge interactions with humans. They are generally user query triggered and fulfill user queries or transactions.

- Autonomous background processes (also known as, background agents): Working behind the scenes to automate routine tasks, analyze data for insights, optimize processes for efficiency, and proactively identify and address potential issues. They include workflow agents. They have limited or no human interaction and are generally driven by events and fulfill queued tasks or chains of tasks.

## Based on number of agents

- Single agent : Operate independently to achieve a specific goal. They utilize external tools and resources to accomplish tasks, enhancing their functional capabilities in diverse environments. They are best suited for well defined tasks that do not require collaboration with other AI agents. Can only handle one foundation model for its processing.

- Multi-agent : Multiple AI agents that collaborate or compete to achieve a common objective or individual goals. These systems leverage the diverse capabilities and roles of individual agents to tackle complex tasks. Multi-agent systems can simulate human behaviors, such as interpersonal communication, in interactive scenarios. Each agent can have different foundation models that best fit their needs.

## Benefits of using AI agents

AI agents can enhance the capabilities of language models by providing autonomy, task automation, and the ability to interact with the real world through tools and embodiment.

### Efficiency and productivity

Increased output : Agents divide tasks like specialized workers, getting more done overall

Simultaneous execution : Agents can work on different things at the same time without getting in each other's way

Automation : Agents take care of repetitive tasks, freeing up humans for more creative work

### Improved decision-making

Collaboration : Agents work together, debate ideas, and learn from each other, leading to better decisions

Adaptability : Agents can adjust their plans and strategies as situations change

Robust reasoning : Through discussion and feedback, agents can refine their reasoning and avoid errors

### Enhanced capabilities

Complex problem-solving : Agents can tackle challenging real-world problems by combining their strengths

Natural language communication : Agents can understand and use human language to interact with people and each other

Tool use : Agents can interact with the external world by using tools and accessing information

Learning and self-improvement : Agents learn from their experiences and get better over time

### Social interaction and simulation

Realistic simulations : Agents can model human-like social behaviors, such as forming relationships and sharing information

Emergent behavior : Complex social interactions can arise organically from the interactions of individual agents

## Challenges with using AI agents

While AI agents offer many benefits, there are also some challenges associated with their use:

Tasks requiring deep empathy / emotional intelligence or requiring complex human interaction and social dynamics – AI agents can struggle with nuanced human emotions. Tasks like therapy, social work, or conflict resolution require a level of emotional understanding and empathy that AI currently lacks. They may falter in complex social situations that require understanding unspoken cues.

Situations with high ethical stakes – AI agents can make decisions based on data, but they lack the moral compass and judgment needed for ethically complex situations. This includes areas like law enforcement, healthcare (diagnosis and treatment), and judicial decision-making.

Domains with unpredictable physical environments – AI agents can struggle in highly dynamic and unpredictable physical environments where real-time adaptation and complex motor skills are essential. This includes tasks like surgery, certain types of construction work, and disaster response.

Resource-intensive applications – Developing and deploying sophisticated AI agents can be computationally expensive and require significant resources, potentially making them unsuitable for smaller projects or organizations with limited budgets.

## Deploy AI agents for scale and efficiency with Cloud Run

AI agents, with their inherent need for flexible compute power to handle reasoning, planning, and tool use, can be an excellent fit for Cloud Run . This fully managed serverless platform allows you to deploy your agent's code—often packaged within a container—as a scalable, reliable service or job. This approach abstracts away infrastructure management, letting developers concentrate on refining the agent's logic.

Cloud Run offers several features that directly support the architecture and demands of sophisticated AI agents:

- Scalability and cost-efficiency: Cloud Run automatically scales the number of container instances up to meet peak demand and, crucially, can scale down to zero when the agent is idle. This means you only pay for the exact compute resources consumed during the agent's active execution, making it cost-effective for goal-oriented, intermittent workloads.

- Agent orchestration and serving: The core agent logic—which manages the model calls, tool selection, and reasoning process—runs as a Cloud Run service. This service provides a stable HTTPS endpoint, making the agent easily accessible via an API for user-facing applications or for communication with other agents

- Agent-to-Agent, or A2A: Frameworks like the Agent Development Kit (ADK) are designed to integrate seamlessly with Cloud Run for easy deployment.

By leveraging Cloud Run's secure, auto-scaling, and flexible environment, organizations can operationalize complex single- or multi-agent systems efficiently.

## Use cases for AI agents

Organizations have been deploying agents to address a variety use cases , which we group into six key broader categories:

## Customer agents

Customer agents

Customer agents deliver personalized customer experiences by understanding customer needs, answering questions, resolving customer issues, or recommending the right products and services. They work seamlessly across multiple channels including the web, mobile, or point of sale, and can be integrated into product experiences with voice or video.

## Employee agents

Employee agents

Employee agents boost productivity by streamlining processes, managing repetitive tasks, answering employee questions, as well as editing and translating critical content and communications.

## Creative agents

Creative agents

Creative agents supercharge the design and creative process by generating content, images, and ideas, assisting with design, writing, personalization, and campaigns.

## Data agents

Data agents

Data agents are built for complex data analysis. They have the potential to find and act on meaningful insights from data, all while ensuring the factual integrity of their results.

## Code agents

Code agents

Code agents accelerate software development with AI-enabled code generation and coding assistance, and to ramp up on new languages and code bases. Many organizations are seeing significant gains in productivity, leading to faster deployment and cleaner, clearer code.

## Security agents

Security agents

Security agents strengthen security posture by mitigating attacks or increasing the speed of investigations. They can oversee security across various surfaces and stages of the security life cycle: prevention, detection, and response.

## Google Cloud and AI agents

Google Cloud provides a portfolio of products and solutions in the AI agent space. These include integrated AI assistants, pre-built AI agents, AI applications, and a platform of agent and developer tools to build custom AI agents.

- Gemini Enterprise App Secure platform to discover, create, run, and govern AI agents across your organization.

- Gemini Enterprise Agent Platform Create AI agents and applications using natural language or a code-first approach. Easily ground your agents or apps in enterprise data with a range of options.

- Customer Experience Agent Studio Build hybrid conversational agents with both deterministic and generative AI functionality.

- Agent Garden Curated collection of pre-built agent samples, solutions, tools, and frameworks to accelerate the development and deployment of AI agents.

- Agent Development Kit (ADK) Open-source Python SDK to build sophisticated multi-agent systems with orchestration, memory, and developer tools.

- A2A Protocol An open-source framework originally developed by Google to help build AI agents. An AI agent built with A2A Protocol will be interoperable with any service, platform, or infrastructure.

- Cloud Run A fully managed serverless platform that allows you to deploy containerized agents and applications, providing auto-scaling and pay-per-use efficiency.

### Additional resources

Continue learning about AI agents with additional resources.

- Google ADK on Github

- Google Agents White Paper (via Kaggle)

- Google Agents Companion White Paper (via Kaggle)

- Skillsboost Advanced Generative AI for Developers Learning

### Take the next step

Start building on Google Cloud with $300 in free credits and 20+ always free products.

- Need help getting started? Contact sales

- Work with a trusted partner Find a partner

- Continue browsing See all products

- Accelerate your digital transformation

- Whether your business is early in its journey or well on its way to digital transformation, Google Cloud can help solve your toughest challenges.

- Learn more

- Key benefits

- Why Google Cloud Top reasons businesses choose us.

- AI and ML Get enterprise-ready AI.

- Multicloud Run your apps wherever you need them.

- Global infrastructure Build on the same infrastructure as Google.

- Data Cloud Make smarter decisions with unified data.

- Modern Infrastructure Cloud Next generation of cloud infrastructure.

- Security Protect your users, data, and apps.

- Productivity and collaboration Connect your teams with AI-powered apps.

- Reports and insights

- Executive insights Curated C-suite perspectives.

- Analyst reports Read what industry analysts say about us.

- Whitepapers Browse and download popular whitepapers.

- Customer stories Explore case studies and videos.

- Industry Solutions

- Application Modernization

- Artificial Intelligence

- APIs and Applications

- Data Analytics

- Databases

- Infrastructure Modernization

- Productivity and Collaboration

- Security

- Startups and SMB

- Industry Solutions Reduce cost, increase operational agility, and capture new market opportunities.

- Retail Analytics and collaboration tools for the retail value chain.

- Consumer Packaged Goods Solutions for CPG digital transformation and brand growth.

- Financial Services Computing, data management, and analytics tools for financial services.

- Healthcare and Life Sciences Advance research at scale and empower healthcare innovation.

- Media and Entertainment Solutions for content production and distribution operations.

- Telecommunications Hybrid and multi-cloud services to deploy and monetize 5G.

- Games AI-driven solutions to build and scale games faster.

- Manufacturing Migration and AI tools to optimize the manufacturing value chain.

- Supply Chain and Logistics Enable sustainable, efficient, and resilient data-driven operations across supply chain and logistics operations.

- Government Data storage, AI, and analytics solutions for government agencies.

- Education Teaching tools to provide more engaging learning experiences.

- Not seeing what you're looking for?

- See all industry solutions

- Application Modernization Assess, plan, implement, and measure software practices and capabilities to modernize and simplify your organization’s business application portfolios.

- CAMP Program that uses DORA to improve your software delivery capabilities.

- Modernize Traditional Applications Analyze, categorize, and get started with cloud migration on traditional workloads.

- Migrate from PaaS: Cloud Foundry, Openshift Tools for moving your existing containers into Google's managed container services.

- Migrate from Mainframe Automated tools and prescriptive guidance for moving your mainframe apps to the cloud.

- Modernize Software Delivery Software supply chain best practices - innerloop productivity, CI/CD and S3C.

- DevOps Best Practices Processes and resources for implementing DevOps in your org.

- SRE Principles Tools and resources for adopting SRE in your org.

- Platform Engineering Comprehensive suite of managed services and Golden Paths to build, manage, and scale IDPs.

- Run Applications at the Edge Guidance for localized and low latency apps on Google’s hardware agnostic edge solution.

- Architect for Multicloud Manage workloads across multiple clouds with a consistent platform.

- Go Serverless Fully managed environment for developing, deploying and scaling apps.

- Artificial Intelligence Add intelligence and efficiency to your business with AI and machine learning.

- Customer Engagement Suite with Google AI End-to-end application that combines our most advanced conversational AI.

- Document AI Document processing and data capture automated at scale.

- Vertex AI Search for commerce Google-quality search and product recommendations for retailers.

- Google Cloud with Gemini AI assistants for application development, coding, and more.

- Generative AI on Google Cloud Transform content creation and discovery, research, customer service, and developer efficiency with the power of generative AI.

- APIs and Applications Speed up the pace of innovation without coding, using APIs, apps, and automation.

- New Business Channels Using APIs Attract and empower an ecosystem of developers and partners.

- Unlocking Legacy Applications Using APIs Cloud services for extending and modernizing legacy apps.

- Open Banking APIx Simplify and accelerate secure delivery of open banking compliant APIs.

- Data Analytics Generate instant insights from data at any scale with a serverless, fully managed analytics platform that significantly simplifies analytics.

- Data Migration Migrate and modernize your data warehouse and data lakes with AI-powered migration services.

- Data Lakehouse Unify and govern your multimodal data with a high-performance and open data lakehouse.

- Real-time Analytics Insights from ingesting, processing, and analyzing event streams.

- Marketing Analytics Solutions for collecting, analyzing, and activating customer data.

- Datasets Data from Google, public, and commercial providers to enrich your analytics and AI initiatives.

- Business Intelligence Solutions for modernizing your BI stack and creating rich data experiences.

- AI for Data Analytics Write SQL, build predictive models, and visualize data with AI for data analytics.

- Geospatial Analytics A comprehensive platform to solve for geospatial use cases at scale.

- Databases Migrate and manage enterprise data with security, reliability, high availability, and fully managed data services.

- Database Migration Guides and tools to simplify your database migration life cycle.

- Database Modernization Upgrades to modernize your operational database infrastructure.

- Databases for Games Build global, live games with Google Cloud databases.

- Google Cloud Databases Database services to migrate, manage, and modernize data.

- Migrate Oracle workloads to Google Cloud Rehost, replatform, rewrite your Oracle workloads.

- Open Source Databases Fully managed open source databases with enterprise-grade support.

- SQL Server on Google Cloud Options for running SQL Server virtual machines on Google Cloud.

- Gemini for Databases Supercharge database development and management with AI.

- Infrastructure Modernization Migrate quickly with solutions for SAP, VMware, Windows, Oracle, and other workloads.

- Application Migration Discovery and analysis tools for moving to the cloud.

- SAP on Google Cloud Certifications for running SAP applications and SAP HANA.

- High Performance Computing Compute, storage, and networking options to support any workload.

- Windows on Google Cloud Tools and partners for running Windows workloads.

- Data Center Migration Migration solutions for VMs, apps, databases, and more.

- Active Assist Automatic cloud resource optimization and increased security.

- Virtual Desktops Remote work solutions for desktops and applications (VDI & DaaS).

- Rapid Migration and Modernization Program End-to-end migration program to simplify your path to the cloud.

- Backup and Disaster Recovery Ensure your business continuity needs are met.

- Red Hat on Google Cloud Google and Red Hat provide an enterprise-grade platform for traditional on-prem and custom applications.

- Cross-Cloud Network Simplify hybrid and multicloud networking, and secure your workloads, data, and users.

- Observability Monitor, troubleshoot, and improve app performance with end-to-end visibility.

- Productivity and Collaboration Change the way teams work with solutions designed for humans and built for impact.

- Google Workspace Collaboration and productivity tools for enterprises.

- Google Workspace Essentials Secure video meetings and modern collaboration for teams.

- Cloud Identity Unified platform for IT admins to manage user devices and apps.

- Chrome Enterprise ChromeOS, Chrome Browser, and Chrome devices built for business.

- Security Detect, investigate, and respond to online threats to help protect your business.

- Agentic SOC Delivering better security outcomes with AI agents.

- Web App and API Protection Threat and fraud protection for your web applications and APIs.

- Security and Resilience Framework Solutions for each phase of the security and resilience life cycle.

- Risk and compliance as code (RCaC) Solution to modernize your governance, risk, and compliance function with automation.

- Software Supply Chain Security Solution for improving end-to-end software supply chain security.

- Security Foundation Recommended products to help achieve a strong security posture.

- Google Cloud Cybershield™ Strengthen nationwide cyber defense.

- Startups and SMB Accelerate startup and SMB growth with tailored solutions and programs.

- Startup Program Get financial, business, and technical support to take your startup to the next level.

- Small and Medium Business Explore solutions for web hosting, app development, AI, and analytics.

- Software as a Service Build better SaaS products, scale efficiently, and grow your business.

- Featured Products

- AI and Machine Learning

- Business Intelligence

- Compute

- Containers

- Data Analytics

- Databases

- Developer Tools

- Distributed Cloud

- Hybrid and Multicloud

- Industry Specific

- Integration Services

- Management Tools

- Maps and Geospatial

- Media Services

- Migration

- Networking

- Operations

- Productivity and Collaboration

- Security and Identity

- Serverless

- Storage

- Web3

- Featured Products

- Compute Engine Virtual machines running in Google’s data center.

- Cloud Storage Object storage that’s secure, durable, and scalable.

- BigQuery Autonomous data to AI platform for analytics and data science.

- Cloud Run Fully managed environment for running containerized apps.

- Google Kubernetes Engine Managed environment for running containerized apps.

- Agent Platform Unified platform for ML models, generative AI, and agent building.

- Looker Platform for BI, data applications, and embedded analytics.

- Apigee API Management Manage the full life cycle of APIs anywhere with visibility and control.

- Cloud SQL Relational database services for MySQL, PostgreSQL and SQL Server.

- Gemini Enterprise app Secure platform to discover, create, run, and govern AI agents for employees.

- Cloud CDN Content delivery network for delivering web and video.

- Not seeing what you're looking for?

- See all products (100+)

- AI and Machine Learning

- Gemini Enterprise Agent Platform Unified platform for ML models, generative AI, and agent building.

- Gemini Enterprise app Secure platform to discover, create, run, and govern AI agents for employees.

- Gemini Enterprise for Customer Experience Build and manage agents that live across the entire customer lifecycle.

- Model Garden Single place to discover over 200 models from Google and Google partners.

- Customer Experience Agent Studio Build conversational AI with both deterministic and gen AI functionality.

- Agent Search Build Google-quality search for your enterprise apps and experiences.

- Speech-to-Text Speech recognition and transcription across 125 languages.

- Text-to-Speech Speech synthesis in 220+ voices and 40+ languages.

- Translation AI Language detection, translation, and glossary support.

- Vision AI Custom and pre-trained models to detect emotion, text, and more.

- Contact Center as a Service Omnichannel contact center solution that is native to the cloud.

- Not seeing what you're looking for?

- See all AI and machine learning products

- Business Intelligence

- Looker Platform for BI, data applications, and embedded analytics.

- Data Studio Interactive data suite for dashboarding, reporting, and analytics.

- Compute

- Compute Engine Virtual machines running in Google’s data center.

- App Engine Serverless application platform for apps and back ends.

- Cloud GPUs GPUs for ML, scientific computing, and 3D visualization.

- Migrate to Virtual Machines Server and virtual machine migration to Compute Engine.

- Spot VMs Compute instances for batch jobs and fault-tolerant workloads.

- Batch Fully managed service for scheduling batch jobs.

- Sole-Tenant Nodes Dedicated hardware for compliance, licensing, and management.

- Bare Metal Infrastructure to run specialized workloads on Google Cloud.

- Recommender Usage recommendations for Google Cloud products and services.

- VMware Engine Fully managed, native VMware Cloud Foundation software stack.

- Cloud Run Fully managed environment for running containerized apps.

- Not seeing what you're looking for?

- See all compute products

- Containers

- Google Kubernetes Engine Managed environment for running containerized apps.

- Cloud Run Fully managed environment for running containerized apps.

- Cloud Build Solution for running build steps in a Docker container.

- Artifact Registry Package manager for build artifacts and dependencies.

- Cloud Code IDE support to write, run, and debug Kubernetes applications.

- Cloud Deploy Fully managed continuous delivery to GKE and Cloud Run.

- Migrate to Containers Components for migrating VMs into system containers on GKE.

- Deep Learning Containers Containers with data science frameworks, libraries, and tools.

- Knative Components to create Kubernetes-native cloud-based software.

- Data Analytics

- BigQuery Autonomous data to AI platform for analytics and data science.

- Managed Service for Apache Spark Zero-ops serverless or managed clusters, accelerated by Lightning Engine.

- Dataflow Real-time analytics for stream and batch processing.

- Looker Platform for BI, data applications, and embedded analytics.

- Lakehouse Open lakehouse platform with enterprise storage and performance capabilities.

- Pub/Sub Messaging service for event ingestion and delivery.

- Managed Service for Apache Airflow Workflow orchestration service built on Apache Airflow.

- Knowledge Catalog Always-on catalog for AI that provides universal context for agents.

- Data Analytics Agents Built-in agents for data lifecycle and tools to build your own agents.

- Data Analytics Migration Services Free-to-use, cloud-native and AI-powered data migration services.

- Managed Service for Apache Kafka Managed Kafka service to operate highly available Apache Kafka clusters.

- Not seeing what you're looking for?

- See all data analytics products

- Databases

- AlloyDB for PostgreSQL Fully managed, PostgreSQL-compatible database for enterprise workloads.

- Cloud SQL Fully managed database for MySQL, PostgreSQL, and SQL Server.

- Firestore Highly scalable and serverless NoSQL document database, with MongoDB compatibility.

- Spanner Cloud-native relational database with unlimited scale and 99.999% availability.

- Bigtable Cloud-native wide-column database for large-scale, low-latency workloads.

- Datastream Serverless change data capture and replication service.

- Database Migration Service Serverless, minimal downtime migrations to Cloud SQL.

- Bare Metal Solution Fully managed infrastructure for your Oracle workloads.

- Memorystore Fully managed Redis and Memcached for sub-millisecond data access.

- Developer Tools

- Artifact Registry Universal package manager for build artifacts and dependencies.

- Cloud Code IDE support to write, run, and debug Kubernetes applications.

- Cloud Build Continuous integration and continuous delivery platform.

- Cloud Deploy Fully managed continuous delivery to GKE and Cloud Run.

- Cloud Deployment Manager Service for creating and managing Google Cloud resources.

- Cloud SDK Command-line tools and libraries for Google Cloud.

- Cloud Scheduler Cron job scheduler for task automation and management.

- Cloud Source Repositories Private Git repository to store, manage, and track code.

- Infrastructure Manager Automate infrastructure management with Terraform.

- Cloud Workstations Managed and secure development environments in the cloud.

- Gemini Code Assist AI-powered assistant available across Google Cloud and your IDE.

- Not seeing what you're looking for?

- See all developer tools

- Distributed Cloud

- Google Distributed Cloud Connected Distributed cloud services for edge workloads.

- Google Distributed Cloud Air-gapped Distributed cloud for air-gapped workloads.

- Hybrid and Multicloud

- Google Kubernetes Engine Managed environment for running containerized apps.

- Apigee API Management API management, development, and security platform.

- Migrate to Containers Tool to move workloads and existing applications to GKE.

- Cloud Build Service for executing builds on Google Cloud infrastructure.

- Observability Monitoring, logging, and application performance suite.

- Cloud Service Mesh Fully managed service mesh based on Envoy and Istio.

- Google Distributed Cloud Fully managed solutions for the edge and data centers.

- Industry Specific

- Anti Money Laundering AI Detect suspicious, potential money laundering activity with AI.

- Cloud Healthcare API Solution for bridging existing care systems and apps on Google Cloud.

- Device Connect for Fitbit Gain a 360-degree patient view with connected Fitbit data on Google Cloud.

- Telecom Network Automation Ready to use cloud-native automation for telecom networks.

- Telecom Data Fabric Telecom data management and analytics with an automated approach.

- Telecom Subscriber Insights Ingests data to improve subscriber acquisition and retention.

- Spectrum Access System (SAS) Controls fundamental access to the Citizens Broadband Radio Service (CBRS).

- Integration Services

- Application Integration Connect to 3rd party apps and enable data consistency without code.

- Workflows Workflow orchestration for serverless products and API services.

- Apigee API Management Manage the full life cycle of APIs anywhere with visibility and control.

- Cloud Tasks Task management service for asynchronous task execution.

- Cloud Scheduler Cron job scheduler for task automation and management.

- Dataproc Service for running Apache Spark and Apache Hadoop clusters.

- Cloud Data Fusion Data integration for building and managing data pipelines.

- Cloud Composer Workflow orchestration service built on Apache Airflow.

- Pub/Sub Messaging service for event ingestion and delivery.

- Eventarc Build an event-driven architecture that can connect any service.

- Management Tools

- Cloud Shell Interactive shell environment with a built-in command line.

- Cloud console Web-based interface for managing and monitoring cloud apps.

- Cloud Endpoints Deployment and development management for APIs on Google Cloud.

- Cloud IAM Permissions management system for Google Cloud resources.

- Cloud APIs Programmatic interfaces for  Google Cloud services.

- Service Catalog Service catalog for admins managing internal enterprise solutions.

- Cost Management Tools for monitoring, controlling, and optimizing your costs.

- Observability Monitoring, logging, and application performance suite.

- Carbon Footprint Dashboard to view and export Google Cloud carbon emissions reports.

- Config Connector Kubernetes add-on for managing Google Cloud resources.

- Active Assist Tools for easily managing performance, security, and cost.

- Not seeing what you're looking for?

- See all management tools

- Maps and Geospatial

- Earth Engine Geospatial platform for Earth observation data and analysis.

- Google Maps Platform Create immersive location experiences and improve business operations.

- Media Services

- Cloud CDN Content delivery network for serving web and video content.

- Live Stream API Service to convert live video and package for streaming.

- OpenCue Open source render manager for visual effects and animation.

- Transcoder API Convert video files and package them for optimized delivery.

- Video Stitcher API Service for dynamic or server side ad insertion.

- Migration

- Migration Center Unified platform for migrating and modernizing with Google Cloud.

- Application Migration App migration to the cloud for low-cost refresh cycles.

- Migrate to Virtual Machines Components for migrating VMs and physical servers to Compute Engine.

- Cloud Foundation Toolkit Reference templates for Deployment Manager and Terraform.

- Database Migration Service Serverless, minimal downtime migrations to Cloud SQL.

- Migrate to Containers Components for migrating VMs into system containers on GKE.

- BigQuery Migration Services Streamlined data warehouse and data lake migration tooling and incentives.

- Rapid Migration and Modernization Program End-to-end migration program to simplify your path to the cloud.

- Transfer Appliance Storage server for moving large volumes of data to Google Cloud.

- Storage Transfer Service Data transfers from online and on-premises sources to Cloud Storage.

- VMware Engine Migrate and run your VMware workloads natively on Google Cloud.

- Networking

- Cloud Armor Security policies and defense against web and DDoS attacks.

- Cloud CDN and Media CDN Content delivery network for serving web and video content.

- Cloud DNS Domain name system for reliable and low-latency name lookups.

- Cloud Load Balancing Service for distributing traffic across applications and regions.

- Cloud NAT NAT service for giving private instances internet access.

- Cloud Connectivity Connectivity options for VPN, peering, and enterprise needs.

- Network Connectivity Center Connectivity management to help simplify and scale networks.

- Network Intelligence Center Network monitoring, verification, and optimization platform.

- Network Service Tiers Cloud network options  based on performance, availability, and cost.

- Virtual Private Cloud Single VPC for an entire organization, isolated within projects.

- Private Service Connect Secure connection between your VPC and services.

- Not seeing what you're looking for?

- See all networking products

- Operations

- Cloud Logging Google Cloud audit, platform, and application logs management.

- Cloud Monitoring Infrastructure and application health with rich metrics.

- Error Reporting Application error identification and analysis.

- Managed Service for Prometheus Fully-managed Prometheus on Google Cloud.

- Cloud Trace Tracing system collecting latency data from applications.

- Cloud Profiler CPU and heap profiler for analyzing application performance.

- Cloud Quotas Manage quotas for all Google Cloud services.

- Productivity and Collaboration

- AppSheet No-code development platform to build and extend applications.

- Gemini Enterprise Secure platform to discover, create, run, and govern AI agents.

- Google Workspace Collaboration and productivity tools for individuals and organizations.

- Google Workspace Essentials Secure video meetings and modern collaboration for teams.

- Cloud Identity Unified platform for IT admins to manage user devices and apps.

- Chrome Enterprise ChromeOS, Chrome browser, and Chrome devices built for business.

- Security and Identity

- Cloud IAM Permissions management system for Google Cloud resources.

- Sensitive Data Protection Discover, classify, and protect your valuable data assets.

- Mandiant Managed Defense Find and eliminate threats with confidence 24x7.

- Google Threat Intelligence Know who’s targeting you.

- Security Command Center Platform for defending against threats to your Google Cloud assets.

- Cloud Key Management Manage encryption keys on Google Cloud.

- Mandiant Incident Response Minimize the impact of a breach.

- Chrome Enterprise Premium Get secure enterprise browsing with extensive endpoint visibility.

- Assured Workloads Compliance and security controls for sensitive workloads.

- Google Security Operations Detect, investigate, and respond to cyber threats.

- Mandiant Consulting Get expert guidance before, during, and after an incident.

- Not seeing what you're looking for?

- See all security and identity products

- Serverless

- Cloud Run Fully managed environment for running containerized apps.

- Cloud Functions Platform for creating functions that respond to cloud events.

- App Engine Serverless application platform for apps and back ends.

- Workflows Workflow orchestration for serverless products and API services.

- API Gateway Develop, deploy, secure, and manage APIs with a fully managed gateway.

- Storage

- Cloud Storage Object storage that’s secure, durable, and scalable.

- Block Storage High-performance storage for AI, analytics, databases, and enterprise applications.

- Filestore File storage that is highly scalable and secure.

- Persistent Disk Block storage for virtual machine instances running on Google Cloud.

- Cloud Storage for Firebase Object storage for storing and serving user-generated content.

- Local SSD Block storage that is locally attached for high-performance needs.

- Storage Transfer Service Data transfers from online and on-premises sources to Cloud Storage.

- Google Cloud Managed Lustre High performance managed parallel file service.

- Google Cloud NetApp Volumes File storage service for NFS, SMB, and multi-protocol environments.

- Backup and DR Service Service for centralized, application-consistent data protection.

- Web3

- Blockchain Node Engine Fully managed node hosting for developing on the blockchain.

- Blockchain RPC Enterprise-grade RPC for building on the blockchain.

- Save money with our transparent approach to pricing

- Google Cloud's pay-as-you-go pricing offers automatic savings based on monthly usage and discounted rates for prepaid resources. Contact us today to get a quote.

- Request a quote

- Pricing overview and tools

- Google Cloud pricing Pay only for what you use with no lock-in.

- Pricing calculator Calculate your cloud savings.

- Google Cloud free tier Explore products with free monthly usage.

- Cost optimization framework Get best practices to optimize workload costs.

- Cost management tools Tools to monitor and control your costs.

- Product-specific Pricing

- Compute Engine

- Cloud SQL

- Google Kubernetes Engine

- Cloud Storage

- BigQuery

- See full price list with 100+ products

- Learn & build

- Google Cloud Free Program $300 in free credits and 20+ free products.

- Solution Generator Get AI generated solution recommendations.

- Quickstarts Get tutorials and walkthroughs.

- Blog Read our latest product news and stories.

- Learning Hub Grow your career with role-based training.

- Google Cloud certification Prepare and register for certifications.

- Cloud computing basics Learn more about cloud computing basics.

- Cloud Architecture Center Get reference architectures and best practices.

- Connect

- Innovators Join Google Cloud's developer program.

- Developer Center Stay in the know and stay connected.

- Events and webinars Browse upcoming and on demand events.

- Google Cloud Community Ask questions, find answers, and connect.

- Consulting and Partners

- Google Cloud Consulting Work with our experts on cloud projects.

- Google Cloud Marketplace Deploy ready-to-go solutions in a few clicks.

- Find a partner Explore the benefits of working with a partner.

- Google Cloud partners Learn about the ecosystem and resources.

- Overview arrow_forward

- Solutions arrow_forward

- Products arrow_forward

- Pricing arrow_forward

- Resources arrow_forward

- Docs

- Support

- Console

- Accelerate your digital transformation

- Learn more

- Key benefits

- Why Google Cloud

- AI and ML

- Multicloud

- Global infrastructure

- Data Cloud

- Modern Infrastructure Cloud

- Security

- Productivity and collaboration

- Reports and insights

- Executive insights

- Analyst reports

- Whitepapers

- Customer stories

- Industry Solutions

- Retail

- Consumer Packaged Goods

- Financial Services

- Healthcare and Life Sciences

- Media and Entertainment

- Telecommunications

- Games

- Manufacturing

- Supply Chain and Logistics

- Government

- Education

- See all industry solutions

- See all solutions

- Application Modernization

- CAMP

- Modernize Traditional Applications

- Migrate from PaaS: Cloud Foundry, Openshift

- Migrate from Mainframe

- Modernize Software Delivery

- DevOps Best Practices

- SRE Principles

- Platform Engineering

- Run Applications at the Edge

- Architect for Multicloud

- Go Serverless

- Artificial Intelligence

- Customer Engagement Suite with Google AI

- Document AI

- Vertex AI Search for commerce

- Google Cloud with Gemini

- Generative AI on Google Cloud

- APIs and Applications

- New Business Channels Using APIs

- Unlocking Legacy Applications Using APIs

- Open Banking APIx

- Data Analytics

- Data Migration

- Data Lakehouse

- Real-time Analytics

- Marketing Analytics

- Datasets

- Business Intelligence

- AI for Data Analytics

- Geospatial Analytics

- Databases

- Database Migration

- Database Modernization

- Databases for Games

- Google Cloud Databases

- Migrate Oracle workloads to Google Cloud

- Open Source Databases

- SQL Server on Google Cloud

- Gemini for Databases

- Infrastructure Modernization

- Application Migration

- SAP on Google Cloud

- High Performance Computing

- Windows on Google Cloud

- Data Center Migration

- Active Assist

- Virtual Desktops

- Rapid Migration and Modernization Program

- Backup and Disaster Recovery

- Red Hat on Google Cloud

- Cross-Cloud Network

- Observability

- Productivity and Collaboration

- Google Workspace

- Google Workspace Essentials

- Cloud Identity

- Chrome Enterprise

- Security

- Agentic SOC

- Web App and API Protection

- Security and Resilience Framework

- Risk and compliance as code (RCaC)

- Software Supply Chain Security

- Security Foundation

- Google Cloud Cybershield™

- Startups and SMB

- Startup Program

- Small and Medium Business

- Software as a Service

- Featured Products

- Compute Engine

- Cloud Storage

- BigQuery

- Cloud Run

- Google Kubernetes Engine

- Agent Platform

- Looker

- Apigee API Management

- Cloud SQL

- Gemini Enterprise app

- Cloud CDN

- See all products (100+)

- AI and Machine Learning

- Gemini Enterprise Agent Platform

- Gemini Enterprise app

- Gemini Enterprise for Customer Experience

- Model Garden

- Customer Experience Agent Studio

- Agent Search

- Speech-to-Text

- Text-to-Speech

- Translation AI

- Vision AI

- Contact Center as a Service

- See all AI and machine learning products

- Business Intelligence

- Looker

- Data Studio

- Compute

- Compute Engine

- App Engine

- Cloud GPUs

- Migrate to Virtual Machines

- Spot VMs

- Batch

- Sole-Tenant Nodes

- Bare Metal

- Recommender

- VMware Engine

- Cloud Run

- See all compute products

- Containers

- Google Kubernetes Engine

- Cloud Run

- Cloud Build

- Artifact Registry

- Cloud Code

- Cloud Deploy

- Migrate to Containers

- Deep Learning Containers

- Knative

- Data Analytics

- BigQuery

- Managed Service for Apache Spark

- Dataflow

- Looker

- Lakehouse

- Pub/Sub

- Managed Service for Apache Airflow

- Knowledge Catalog

- Data Analytics Agents

- Data Analytics Migration Services

- Managed Service for Apache Kafka

- See all data analytics products

- Databases

- AlloyDB for PostgreSQL

- Cloud SQL

- Firestore

- Spanner

- Bigtable

- Datastream

- Database Migration Service

- Bare Metal Solution

- Memorystore

- Developer Tools

- Artifact Registry

- Cloud Code

- Cloud Build

- Cloud Deploy

- Cloud Deployment Manager

- Cloud SDK

- Cloud Scheduler

- Cloud Source Repositories

- Infrastructure Manager

- Cloud Workstations

- Gemini Code Assist

- See all developer tools

- Distributed Cloud

- Google Distributed Cloud Connected

- Google Distributed Cloud Air-gapped

- Hybrid and Multicloud

- Google Kubernetes Engine

- Apigee API Management

- Migrate to Containers

- Cloud Build

- Observability

- Cloud Service Mesh

- Google Distributed Cloud

- Industry Specific

- Anti Money Laundering AI

- Cloud Healthcare API

- Device Connect for Fitbit

- Telecom Network Automation

- Telecom Data Fabric

- Telecom Subscriber Insights

- Spectrum Access System (SAS)

- Integration Services

- Application Integration

- Workflows

- Apigee API Management

- Cloud Tasks

- Cloud Scheduler

- Dataproc

- Cloud Data Fusion

- Cloud Composer

- Pub/Sub

- Eventarc

- Management Tools

- Cloud Shell

- Cloud console

- Cloud Endpoints

- Cloud IAM

- Cloud APIs

- Service Catalog

- Cost Management

- Observability

- Carbon Footprint

- Config Connector

- Active Assist

- See all management tools

- Maps and Geospatial

- Earth Engine

- Google Maps Platform

- Media Services

- Cloud CDN

- Live Stream API

- OpenCue

- Transcoder API

- Video Stitcher API

- Migration

- Migration Center

- Application Migration

- Migrate to Virtual Machines

- Cloud Foundation Toolkit

- Database Migration Service

- Migrate to Containers

- BigQuery Migration Services

- Rapid Migration and Modernization Program

- Transfer Appliance

- Storage Transfer Service

- VMware Engine

- Networking

- Cloud Armor

- Cloud CDN and Media CDN

- Cloud DNS

- Cloud Load Balancing

- Cloud NAT

- Cloud Connectivity

- Network Connectivity Center

- Network Intelligence Center

- Network Service Tiers

- Virtual Private Cloud

- Private Service Connect

- See all networking products

- Operations

- Cloud Logging

- Cloud Monitoring

- Error Reporting

- Managed Service for Prometheus

- Cloud Trace

- Cloud Profiler

- Cloud Quotas

- Productivity and Collaboration

- AppSheet

- Gemini Enterprise

- Google Workspace

- Google Workspace Essentials

- Cloud Identity

- Chrome Enterprise

- Security and Identity

- Cloud IAM

- Sensitive Data Protection

- Mandiant Managed Defense

- Google Threat Intelligence

- Security Command Center

- Cloud Key Management

- Mandiant Incident Response

- Chrome Enterprise Premium

- Assured Workloads

- Google Security Operations

- Mandiant Consulting

- See all security and identity products

- Serverless

- Cloud Run

- Cloud Functions

- App Engine

- Workflows

- API Gateway

- Storage

- Cloud Storage

- Block Storage

- Filestore

- Persistent Disk

- Cloud Storage for Firebase

- Local SSD

- Storage Transfer Service

- Google Cloud Managed Lustre

- Google Cloud NetApp Volumes

- Backup and DR Service

- Web3

- Blockchain Node Engine

- Blockchain RPC

- Save money with our transparent approach to pricing

- Request a quote

- Pricing overview and tools

- Google Cloud pricing

- Pricing calculator

- Google Cloud free tier

- Cost optimization framework

- Cost management tools

- Product-specific Pricing

- Compute Engine

- Cloud SQL

- Google Kubernetes Engine

- Cloud Storage

- BigQuery

- See full price list with 100+ products

- Learn & build

- Google Cloud Free Program

- Solution Generator

- Quickstarts

- Blog

- Learning Hub

- Google Cloud certification

- Cloud computing basics

- Cloud Architecture Center

- Connect

- Innovators

- Developer Center

- Events and webinars

- Google Cloud Community

- Consulting and Partners

- Google Cloud Consulting

- Google Cloud Marketplace

- Find a partner

- Google Cloud partners

- Why Google Choosing Google Cloud Trust and security Modern Infrastructure Cloud Multicloud Global infrastructure Locations Customers and case studies Analyst reports Whitepapers Blog


# Compile

To compile means to gather information from various sources and arrange it into a structured format, such as a report, list, book, or file. In computing, it refers to translating human-readable source code into machine-readable, executable instructions.

## Key Definitions of Compile

*   **Gathering Information**: To collect and put together data, facts, or documents (e.g., to compile a report or compile a list).
*   **Creating Works**: To produce a book, anthology, or database from various materials.
*   **Computing**: To convert high-level programming code (like C++ or Java) into machine code, allowing a computer to execute the program.

## Usage Examples

*   "She is compiling a list of clients for the newsletter."
*   "It took years to compile the dictionary."
*   "The developer needs to compile the code before running the application."

## Synonyms

*   Assemble
*   Collect
*   Gather
*   Compose
*   Accumulate
*   Organize
*   Synthesize

## Contextual Usage

*   **General**: Focuses on the act of assembling information or materials (e.g., compile a report).
*   **Computing**: Focuses on the automatic transformation of code using a tool known as a compiler.

## Gemini CLI Subagents

# Subagents

Subagents are specialized agents that operate within your main Gemini CLI session. They are designed to handle specific, complex tasks—like deep codebase analysis, documentation lookup, or domain-specific reasoning—without cluttering the main agent’s context or toolset.

## What are subagents?
Subagents are “specialists” that the main Gemini agent can hire for a specific job.

*   **Focused context:** Each subagent has its own system prompt and persona.
*   **Specialized tools:** Subagents can have a restricted or specialized set of tools.
*   **Independent context window:** Interactions with a subagent happen in a separate context loop, which saves tokens in your main conversation history.

Subagents are exposed to the main agent as a tool of the same name. When the main agent calls the tool, it delegates the task to the subagent. Once the subagent completes its task, it reports back to the main agent with its findings.

## How to use subagents
You can use subagents through automatic delegation or by explicitly forcing them in your prompt.

### Automatic delegation
Gemini CLI’s main agent is instructed to use specialized subagents when a task matches their expertise. For example, if you ask “How does the auth system work?”, the main agent may decide to call the `codebase_investigator` subagent to perform the research.

### Forcing a subagent (@ syntax)
You can explicitly direct a task to a specific subagent by using the `@` symbol followed by the subagent’s name at the beginning of your prompt. This is useful when you want to bypass the main agent’s decision-making and go straight to a specialist.

Example:

**Terminal window**
`@codebase_investigator Map out the relationship between the AgentRegistry and the LocalAgentExecutor.`

When you use the `@` syntax, the CLI injects a system note that nudges the primary model to use that specific subagent tool immediately.

## Built-in subagents
Gemini CLI comes with the following built-in subagents:

### Codebase Investigator
*   **Name:** `codebase_investigator`
*   **Purpose:** Analyze the codebase, reverse engineer, and understand complex dependencies.
*   **When to use:** “How does the authentication system work?”, “Map out the dependencies of the AgentRegistry class.”
*   **Configuration:** Enabled by default. You can override its settings in `settings.json` under `agents.overrides`. Example (forcing a specific model and increasing turns):

```json
{
  "agents": {
    "overrides": {
      "codebase_investigator": {
        "modelConfig": { "model": "gemini-3-flash-preview" },
        "runConfig": { "maxTurns": 50 }
      }
    }
  }
}
```

### CLI Help Agent
*   **Name:** `cli_help`
*   **Purpose:** Get expert knowledge about Gemini CLI itself, its commands, configuration, and documentation.
*   **When to use:** “How do I configure a proxy?”, “What does the /rewind command do?”
*   **Configuration:** Enabled by default.

### Generalist Agent
*   **Name:** `generalist`
*   **Purpose:** A general, all-purpose subagent that uses the inherited tool access and configurations from the main agent. Useful for executing broad, resource-heavy subtasks in an isolated conversation, optimizing your main agent’s context by returning only the final result of that given task.
*   **When to use:** Use this agent when a task requires many steps, handles large volumes of information, or requires the same full capabilities as the main agent. It is ideal for:
    *   **Multi-file modifications:** Applying refactors or fixing errors across several files at once.
    *   **High-volume execution:** Running commands or tests that produce extensive terminal output.
    *   **Action-oriented research:** Investigations where the agent needs to both search code and run commands or make edits to find a solution. By delegating these tasks, you prevent your main conversation from becoming cluttered or slow. You can invoke it explicitly using `@generalist`.
*   **Configuration:** Enabled by default.

### Browser Agent (experimental)
*   **Name:** `browser_agent`
*   **Purpose:** Automate web browser tasks — navigating websites, filling forms, clicking buttons, and extracting information from web pages — using the accessibility tree.
*   **When to use:** “Go to example.com and fill out the contact form,” “Extract the pricing table from this page,” “Click the login button and enter my credentials.”

> **Note**
> This is a preview feature currently under active development.

#### Prerequisites
The browser agent requires:

*   **Chrome version 144 or later** (any recent stable release works).
*   The underlying `chrome-devtools-mcp` server is bundled with Gemini CLI and launched automatically — no separate installation is needed.

#### Enabling the browser agent
The browser agent is disabled by default. Enable it in your `settings.json`:

```json
{
  "agents": {
    "overrides": {
      "browser_agent": {
        "enabled": true
      }
    }
  }
}
```

#### Session modes
The `sessionMode` setting controls how Chrome is launched and managed. Set it under `agents.browser`:

```json
{
  "agents": {
    "overrides": {
      "browser_agent": {
        "enabled": true
      }
    },
    "browser": {
      "sessionMode": "persistent"
    }
  }
}
```

The available modes are:

| Mode | Description |
| :--- | :--- |
| `persistent` | **(Default)** Launches Chrome with a persistent profile stored at `~/.gemini/cli-browser-profile/`. Cookies, history, and settings are preserved between sessions. |
| `isolated` | Launches Chrome with a temporary profile that is deleted after each session. Use this for clean-state automation. |
| `existing` | Attaches to an already-running Chrome instance. You must enable remote debugging first by navigating to `chrome://inspect/#remote-debugging` in Chrome. No new browser process is launched. |

#### First-run consent
The first time the browser agent is invoked, Gemini CLI displays a consent dialog. You must accept before the browser session starts. This dialog only appears once.

#### Configuration reference
All browser-specific settings go under `agents.browser` in your `settings.json`. For full details, see the `agents.browser` configuration reference.

| Setting | Type | Default | Description |
| :--- | :--- | :--- | :--- |
| `sessionMode` | `string` | `"persistent"` | How Chrome is managed: `"persistent"`, `"isolated"`, or `"existing"`. |
| `headless` | `boolean` | `false` | Run Chrome in headless mode (no visible window). |
| `profilePath` | `string` | — | Custom path to a browser profile directory. |
| `visualModel` | `string` | — | Model override for the visual agent. |
| `allowedDomains` | `string[]` | — | Restrict navigation to specific domains (for example, `["github.com"]`). |
| `disableUserInput` | `boolean` | `true` | Disable user input on the browser window during automation (non-headless only). |
| `maxActionsPerTask` | `number` | `100` | Maximum tool calls per task. The agent is terminated when the limit is reached. |
| `confirmSensitiveActions` | `boolean` | `false` | Require manual confirmation for `upload_file` and `evaluate_script`. |
| `blockFileUploads` | `boolean` | `false` | Hard-block all file upload requests from the agent. |

#### Automation overlay and input blocking
In non-headless mode, the browser agent injects a visual overlay into the browser window to indicate that automation is in progress. By default, user input (keyboard and mouse) is also blocked to prevent accidental interference. You can disable this by setting `disableUserInput` to `false`.

#### Security
The browser agent enforces several layers of security:

*   **Domain restrictions:** When `allowedDomains` is set, the agent can only navigate to the listed domains (and their subdomains when using `*.` prefix). Attempting to visit a disallowed domain throws a fatal error that immediately terminates the agent. The agent also attempts to detect and block the use of allowed domains as proxies (e.g., via query parameters or fragments) to access restricted content.
*   **Blocked URL patterns:** The underlying MCP server blocks dangerous URL schemes including `file://`, `javascript:`, `data:text/html`, `chrome://extensions`, and `chrome://settings/passwords`.
*   **Sensitive action confirmation:** Form filling (`fill`, `fill_form`) always requires user confirmation through the policy engine, regardless of approval mode. When `confirmSensitiveActions` is `true`, `upload_file` and `evaluate_script` also require confirmation.
*   **File upload blocking:** Set `blockFileUploads` to `true` to hard-block all file upload requests, preventing the agent from uploading any files.
*   **Action rate limiting:** The `maxActionsPerTask` setting (default: 100) limits the total number of tool calls per task to prevent runaway execution.

#### Visual agent
By default, the browser agent interacts with pages through the accessibility tree using element `uid` values. For tasks that require visual identification (for example, “click the yellow button” or “find the red error message”), you can enable the visual agent by setting a `visualModel`:

```json
{
  "agents": {
    "overrides": {
      "browser_agent": {
        "enabled": true
      }
    },
    "browser": {
      "visualModel": "gemini-2.5-computer-use-preview-10-2025"
    }
  }
}
```

When enabled, the agent gains access to the `analyze_screenshot` tool, which captures a screenshot and sends it to the vision model for analysis. The model returns coordinates and element descriptions that the browser agent uses with the `click_at` tool for precise, coordinate-based interactions.

> **Note**
> The visual agent requires API key or Vertex AI authentication. It is not available when using “Sign in with Google”.

#### Sandbox support
The browser agent adjusts its behavior automatically when running inside a sandbox.

**macOS seatbelt (sandbox-exec)**
When the CLI runs under the macOS seatbelt sandbox, `persistent` and `isolated` session modes are forced to `isolated` with headless enabled. This avoids permission errors caused by seatbelt file-system restrictions on persistent browser profiles. If `sessionMode` is set to `existing`, no override is applied.

**Container sandboxes (Docker / Podman)**
Chrome is not available inside the container, so the browser agent is disabled unless `sessionMode` is set to `"existing"`. When enabled with existing mode, the agent automatically connects to Chrome on the host via the resolved IP of `host.docker.internal:9222` instead of using local pipe discovery. Port `9222` is currently hardcoded and cannot be customized.

To use the browser agent in a Docker sandbox:

1.  Start Chrome on the host with remote debugging enabled:

    **Terminal window**
    ```bash
    # Option A: Launch Chrome from the command line
    google-chrome --remote-debugging-port=9222

    # Option B: Enable in Chrome settings
    # Navigate to chrome://inspect/#remote-debugging and enable
    ```
2.  Configure `sessionMode` and allowed domains in your project’s `.gemini/settings.json`:

    ```json
    {
      "agents": {
        "overrides": {
          "browser_agent": { "enabled": true }
        },
        "browser": {
          "sessionMode": "existing",
          "allowedDomains": ["example.com"]
        }
      }
    }
    ```
3.  Launch the CLI with port forwarding:

    **Terminal window**
    ```bash
    GEMINI_SANDBOX=docker SANDBOX_PORTS=9222 gemini
    ```

## Creating custom subagents
You can create your own subagents to automate specific workflows or enforce specific personas.

### Agent definition files
Custom agents are defined as Markdown files (`.md`) with YAML frontmatter. You can place them in:

*   **Project-level:** `.gemini/agents/*.md` (Shared with your team)
*   **User-level:** `~/.gemini/agents/*.md` (Personal agents)

### File format
The file MUST start with YAML frontmatter enclosed in triple-dashes `---`. The body of the markdown file becomes the agent’s System Prompt.

Example: `.gemini/agents/security-auditor.md`

```yaml
---
name: security-auditor
description: Specialized in finding security vulnerabilities in code.
kind: local
tools:
  - read_file
  - grep_search
model: gemini-3-flash-preview
temperature: 0.2
max_turns: 10
---
```

You are a ruthless Security Auditor. Your job is to analyze code for potential
vulnerabilities.

Focus on:

1.  SQL Injection
2.  XSS (Cross-Site Scripting)
3.  Hardcoded credentials
4.  Unsafe file operations

When you find a vulnerability, explain it clearly and suggest a fix. Do not fix
it yourself; just report it.

### Configuration schema

| Field | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| `name` | `string` | **Yes** | Unique identifier (slug) used as the tool name for the agent. Only lowercase letters, numbers, hyphens, and underscores. |
| `description` | `string` | **Yes** | Short description of what the agent does. This is visible to the main agent to help it decide when to call this subagent. |
| `kind` | `string` | No | `local` (default) or `remote`. |
| `tools` | `array` | No | List of tool names this agent can use. Supports wildcards: `*` (all tools), `mcp_*` (all MCP tools), `mcp_server_*` (all tools from a server). If omitted, it inherits all tools from the parent session. |
| `mcpServers` | `object` | No | Configuration for inline Model Context Protocol (MCP) servers isolated to this specific agent. |
| `model` | `string` | No | Specific model to use (for example, `gemini-3-preview`). Defaults to `inherit` (uses the main session model). |
| `temperature` | `number` | No | Model temperature (0.0 - 2.0). Defaults to `1`. |
| `max_turns` | `number` | No | Maximum number of conversation turns allowed for this agent before it must return. Defaults to `30`. |
| `timeout_mins` | `number` | No | Maximum execution time in minutes. Defaults to `10`. |

### Tool wildcards
When defining tools for a subagent, you can use wildcards to quickly grant access to groups of tools:

*   `*`: Grant access to all available built-in and discovered tools.
*   `mcp_*`: Grant access to all tools from all connected MCP servers.
*   `mcp_my-server_*`: Grant access to all tools from a specific MCP server named `my-server`.

### Isolation and recursion protection
Each subagent runs in its own isolated context loop. This means:

*   **Independent history:** The subagent’s conversation history does not bloat the main agent’s context.
*   **Isolated tools:** The subagent only has access to the tools you explicitly grant it.
*   **Recursion protection:** To prevent infinite loops and excessive token usage, subagents cannot call other subagents. If a subagent is granted the `*` tool wildcard, it will still be unable to see or invoke other agents.

## Subagent tool isolation
Subagent tool isolation moves Gemini CLI away from a single global tool registry. By providing isolated execution environments, you can ensure that subagents only interact with the parts of the system they are designed for. This prevents unintended side effects, improves reliability by avoiding state contamination, and enables fine-grained permission control.

With this feature, you can:

*   **Specify tool access:** Define exactly which tools an agent can access using a `tools` list in the agent definition.
*   **Define inline MCP servers:** Configure Model Context Protocol (MCP) servers (which provide a standardized way to connect AI models to external tools and data sources) directly in the subagent’s markdown frontmatter, isolating them to that specific agent.
*   **Maintain state isolation:** Ensure that subagents only interact with their own set of tools and servers, preventing side effects and state contamination.
*   **Apply subagent-specific policies:** Enforce granular rules in your Policy Engine TOML configuration based on the executing subagent’s name.

### Configuring isolated tools and servers
You can configure tool isolation for a subagent by updating its markdown frontmatter. This lets you explicitly state which tools the subagent can use, rather than relying on the global registry.

Add an `mcpServers` object to define inline MCP servers that are unique to the agent.

Example:

```yaml
---
name: my-isolated-agent
tools:
  - grep_search
  - read_file
mcpServers:
  my-custom-server:
    command: 'node'
    args: ['path/to/server.js']
---
```

### Subagent-specific policies
You can enforce fine-grained control over subagents using the Policy Engine’s TOML configuration. This allows you to grant or restrict permissions specifically for an agent, without affecting the rest of your CLI session.

To restrict a policy rule to a specific subagent, add the `subagent` property to the `[[rules]]` block in your `policy.toml` file.

Example:

```toml
[[rules]]
name = "Allow pr-creator to push code"
subagent = "pr-creator"
description = "Permit pr-creator to push branches automatically."
action = "allow"
toolName = "run_shell_command"
commandPrefix = "git push"
```

In this configuration, the policy rule only triggers if the executing subagent’s name matches `pr-creator`. Rules without the `subagent` property apply universally to all agents.

## Managing subagents
You can manage subagents interactively using the `/agents` command or persistently via `settings.json`.

### Interactive management (/agents)
If you are in an interactive CLI session, you can use the `/agents` command to manage subagents without editing configuration files manually. This is the recommended way to quickly enable, disable, or re-configure agents on the fly.

For a full list of sub-commands and usage, see the `/agents` command reference.

### Persistent configuration (settings.json)
While the `/agents` command and agent definition files provide a starting point, you can use `settings.json` for global, persistent overrides. This is useful for enforcing specific models or execution limits across all sessions.

`agents.overrides`
Use this to enable or disable specific agents or override their run configurations.

```json
{
  "agents": {
    "overrides": {
      "security-auditor": {
        "enabled": false,
        "runConfig": {
          "maxTurns": 20,
          "maxTimeMinutes": 10
        }
      }
    }
  }
}
```

`modelConfigs.overrides`
You can target specific subagents with custom model settings (like system instruction prefixes or specific safety settings) using the `overrideScope` field.

```json
{
  "modelConfigs": {
    "overrides": [
      {
        "match": { "overrideScope": "security-auditor" },
        "modelConfig": {
          "generateContentConfig": {
            "temperature": 0.1
          }
        }
      }
    ]
  }
}
```

### Safety policies (TOML)
You can restrict access to specific subagents using the CLI’s Policy Engine. Subagents are treated as virtual tool names for policy matching purposes.

To govern access to a subagent, create a `.toml` file in your policy directory (e.g., `~/.gemini/policies/`):

```toml
[[rule]]
toolName = "codebase_investigator"
decision = "deny"
deny_message = "Deep codebase analysis is restricted for this session."
```

For more information on setting up fine-grained safety guardrails, see the Policy Engine reference.

## Optimizing your subagent
The main agent’s system prompt encourages it to use an expert subagent when one is available. It decides whether an agent is a relevant expert based on the agent’s description. You can improve the reliability with which an agent is used by updating the description to more clearly indicate:

*   Its area of expertise.
*   When it should be used.
*   Some example scenarios.

For example, the following subagent description should be called fairly consistently for Git operations.

> Git expert agent which should be used for all local and remote git operations. For example:
> *   Making commits
> *   Searching for regressions with bisect
> *   Interacting with source control and issues providers such as GitHub.

If you need to further tune your subagent, you can do so by selecting the model to optimize for with `/model` and then asking the model why it does not think that your subagent was called with a specific prompt and the given description.

## Remote subagents (Agent2Agent)
Gemini CLI can also delegate tasks to remote subagents using the Agent-to-Agent (A2A) protocol.

See the Remote Subagents documentation for detailed configuration, authentication, and usage instructions.

## Extension subagents
Extensions can bundle and distribute subagents. See the Extensions documentation for details on how to package agents within an extension.

## Disabling subagents
Subagents are enabled by default. To disable them, set `enableAgents` to `false` in your `settings.json`:

```json
{
  "experimental": { "enableAgents": false }
}
```
