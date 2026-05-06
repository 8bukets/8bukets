# What are AI Agents?

Scraped from [https://cloud.google.com/discover/what-are-ai-agents](https://cloud.google.com/discover/what-are-ai-agents)

## What is an AI agent?

Last Updated: 04/02/2026

AI agents are software systems that use AI to pursue goals and complete tasks on behalf of users. They show reasoning, planning, and memory and have a level of autonomy to make decisions, learn, and adapt.

Their capabilities are made possible in large part by the multimodal capacity of generative AI and AI foundation models. AI agents can process multimodal information like text, voice, video, audio, code, and more simultaneously; can converse, reason, learn, and make decisions. They can learn over time and facilitate transactions and business processes. Agents can work with other agents to coordinate and perform more complex workflows.

## Key features of an AI agent

As explained above, while the key features of an AI agent are reasoning and acting (as described in ReAct Framework ) more features have evolved over time.

- Reasoning:This core cognitive process involves using logic and available information to draw conclusions, make inferences, and solve problems. AI agents with strong reasoning capabilities can analyze data, identify patterns, and make informed decisions based on evidence and context.

- Acting: The ability to take action or perform tasks based on decisions, plans, or external input is crucial for AI agents to interact with their environment and achieve goals. This can include physical actions in the case of embodied AI, or digital actions like sending messages, updating data, or triggering other processes.

- Observing: Gathering information about the environment or situation through perception or sensing is essential for AI agents to understand their context and make informed decisions. This can involve various forms of perception, such as computer vision, natural language processing, or sensor data analysis.

- Planning: Developing a strategic plan to achieve goals is a key aspect of intelligent behavior. AI agents with planning capabilities can identify the necessary steps, evaluate potential actions, and choose the best course of action based on available information and desired outcomes. This often involves anticipating future states and considering potential obstacles.

- Collaborating: Working effectively with others, whether humans or other AI agents, to achieve a common goal is increasingly important in complex and dynamic environments. Collaboration requires communication, coordination, and the ability to understand and respect the perspectives of others.

- Self-refining: The capacity for self-improvement and adaptation is a hallmark of advanced AI systems. AI agents with self-refining capabilities can learn from experience, adjust their behavior based on feedback, and continuously enhance their performance and capabilities over time. This can involve machine learning techniques, optimization algorithms, or other forms of self-modification.

## What is the difference between AI agents, AI assistants, and bots?

AI assistants are AI agents designed as applications or products to collaborate directly with users and perform tasks by understanding and responding to natural human language and inputs. They can reason and take action on the users' behalf with their supervision.

AI assistants are often embedded in the product being used. A key characteristic is the interaction between the assistant and user through the different steps of the task. The assistant responds to requests or prompts from the user, and can recommend actions but decision-making is done by the user.


 | AI agent | AI assistant | Bot﻿
Purpose | Autonomously and proactively perform tasks | Assisting users with tasks | Automating simple tasks or conversations
Capabilities | Can perform complex, multi-step actions; learns and adapts; can make decisions independently | Responds to requests or prompts; provides information and completes simple tasks; can recommend actions but the user makes decisions | Follows pre-defined rules; limited learning; basic interactions
Interaction | Proactive; goal-oriented | Reactive; responds to user requests | Reactive; responds to triggers or commands

## Key differences

- Autonomy: AI agents have the highest degree of autonomy, able to operate and make decisions independently to achieve a goal. AI assistants are less autonomous, requiring user input and direction. Bots are the least autonomous, typically following pre-programmed rules.

- Complexity: AI agents are designed to handle complex tasks and workflows, while AI assistants and bots are better suited for simpler tasks and interactions.

- Learning: AI agents often employ machine learning to adapt and improve their performance over time. AI assistants may have some learning capabilities, while bots typically have limited or no learning.

## How do AI agents work?

Every agent defines its role, personality, and communication style, including specific instructions and descriptions of available tools.

- Persona: A well defined persona allows an agent to maintain a consistent character and behave in a manner appropriate to its assigned role, evolving as the agent gains experience and interacts with its environment.

- Memory: The agent is equipped in general with short term, long term, consensus, and episodic memory. Short term memory for immediate interactions, long-term memory for historical data and conversations, episodic memory for past interactions, and consensus memory for shared information among agents. The agent can maintain context, learn from experiences, and improve performance by recalling past interactions and adapting to new situations.

- Tools: Tools are functions or external resources that an agent can utilize to interact with its environment and enhance its capabilities. They allow agents to perform complex tasks by accessing information, manipulating data, or controlling external systems, and can be categorized based on their user interface, including physical, graphical, and program-based interfaces. Tool learning involves teaching agents how to effectively use these tools by understanding their functionalities and the context in which they should be applied.

- Model: Large language models (LLMs) serve as the foundation for building AI agents, providing them with the ability to understand, reason, and act. LLMs act as the "brain" of an agent, enabling them to process and generate language, while other components facilitate reason and action.

## What are the types of agents in AI?

AI agents can be categorized in various ways based on their capabilities, roles, and environments. Here are some key categories of agents:

There are different definitions of agent types and agent categories.

## Based on interaction

One way to categorize agents is by how they interact with users. Some agents engage in direct conversation, while others operate in the background, performing tasks without direct user input:

- Interactive partners(also known as, surface agents): Assisting us with tasks like customer service, healthcare, education, and scientific discovery, providing personalized and intelligent support. Conversational agents include Q&A, chit chat, and world knowledge interactions with humans. They are generally user query triggered and fulfill user queries or transactions.

- Autonomous background processes(also known as, background agents): Working behind the scenes to automate routine tasks, analyze data for insights, optimize processes for efficiency, and proactively identify and address potential issues. They include workflow agents. They have limited or no human interaction and are generally driven by events and fulfill queued tasks or chains of tasks.

## Based on number of agents

- Single agent: Operate independently to achieve a specific goal. They utilize external tools and resources to accomplish tasks, enhancing their functional capabilities in diverse environments. They are best suited for well defined tasks that do not require collaboration with other AI agents. Can only handle one foundation model for its processing.

- Multi-agent: Multiple AI agents that collaborate or compete to achieve a common objective or individual goals. These systems leverage the diverse capabilities and roles of individual agents to tackle complex tasks. Multi-agent systems can simulate human behaviors, such as interpersonal communication, in interactive scenarios. Each agent can have different foundation models that best fit their needs.

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

- Scalability and cost-efficiency:Cloud Run automatically scales the number of container instances up to meet peak demand and, crucially, can scale down to zero when the agent is idle. This means you only pay for the exact compute resources consumed during the agent's active execution, making it cost-effective for goal-oriented, intermittent workloads.

- Agent orchestration and serving:The core agent logic—which manages the model calls, tool selection, and reasoning process—runs as a Cloud Run service. This service provides a stable HTTPS endpoint, making the agent easily accessible via an API for user-facing applications or for communication with other agents

- Agent-to-Agent, or A2A:Frameworks like theAgent Development Kit(ADK) are designed to integrate seamlessly with Cloud Run for easy deployment.

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

- Gemini Enterprise AppSecure platform to discover, create, run, and govern AI agents across your organization.

- Gemini Enterprise Agent PlatformCreate AI agents and applications using natural language or a code-first approach. Easily ground your agents or apps in enterprise data with a range of options.

- Customer Experience Agent StudioBuild hybrid conversational agents with both deterministic and generative AI functionality.

- Agent GardenCurated collection of pre-built agent samples, solutions, tools, and frameworks to accelerate the development and deployment of AI agents.

- Agent Development Kit (ADK)Open-source Python SDK to build sophisticated multi-agent systems with orchestration, memory, and developer tools.

- A2A ProtocolAn open-source framework originally developed by Google to help build AI agents. An AI agent built with A2A Protocol will be interoperable with any service, platform, or infrastructure.

- Cloud RunA fully managed serverless platform that allows you to deploy containerized agents and applications, providing auto-scaling and pay-per-use efficiency.

### Additional resources

Continue learning about AI agents with additional resources.

- Google ADK on Github

- Google Agents White Paper (via Kaggle)

- Google Agents Companion White Paper (via Kaggle)

- Skillsboost Advanced Generative AI for Developers Learning

### Take the next step

Start building on Google Cloud with $300 in free credits and 20+ always free products.

- Need help getting started?Contact sales

- Work with a trusted partnerFind a partner

- Continue browsingSee all products

- Accelerate your digital transformation

- Whether your business is early in its journey or well on its way to digital transformation, Google Cloud can help solve your toughest challenges.

- Learn more

- Key benefits

- Why Google CloudTop reasons businesses choose us.

- AI and MLGet enterprise-ready AI.

- MulticloudRun your apps wherever you need them.

- Global infrastructureBuild on the same infrastructure as Google.

- Data CloudMake smarter decisions with unified data.

- Modern Infrastructure CloudNext generation of cloud infrastructure.

- SecurityProtect your users, data, and apps.

- Productivity and collaborationConnect your teams with AI-powered apps.

- Reports and insights

- Executive insightsCurated C-suite perspectives.

- Analyst reportsRead what industry analysts say about us.

- WhitepapersBrowse and download popular whitepapers.

- Customer storiesExplore case studies and videos.

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

- Industry SolutionsReduce cost, increase operational agility, and capture new market opportunities.

- RetailAnalytics and collaboration tools for the retail value chain.

- Consumer Packaged GoodsSolutions for CPG digital transformation and brand growth.

- Financial ServicesComputing, data management, and analytics tools for financial services.

- Healthcare and Life SciencesAdvance research at scale and empower healthcare innovation.

- Media and EntertainmentSolutions for content production and distribution operations.

- TelecommunicationsHybrid and multi-cloud services to deploy and monetize 5G.

- GamesAI-driven solutions to build and scale games faster.

- ManufacturingMigration and AI tools to optimize the manufacturing value chain.

- Supply Chain and LogisticsEnable sustainable, efficient, and resilient data-driven operations across supply chain and logistics operations.

- GovernmentData storage, AI, and analytics solutions for government agencies.

- EducationTeaching tools to provide more engaging learning experiences.

- Not seeing what you're looking for?

- See all industry solutions

- Application ModernizationAssess, plan, implement, and measure software practices and capabilities to modernize and simplify your organization’s business application portfolios.

- CAMPProgram that uses DORA to improve your software delivery capabilities.

- Modernize Traditional ApplicationsAnalyze, categorize, and get started with cloud migration on traditional workloads.

- Migrate from PaaS: Cloud Foundry, OpenshiftTools for moving your existing containers into Google's managed container services.

- Migrate from MainframeAutomated tools and prescriptive guidance for moving your mainframe apps to the cloud.

- Modernize Software DeliverySoftware supply chain best practices - innerloop productivity, CI/CD and S3C.

- DevOps Best PracticesProcesses and resources for implementing DevOps in your org.

- SRE PrinciplesTools and resources for adopting SRE in your org.

- Platform EngineeringComprehensive suite of managed services and Golden Paths to build, manage, and scale IDPs.

- Run Applications at the EdgeGuidance for localized and low latency apps on Google’s hardware agnostic edge solution.

- Architect for MulticloudManage workloads across multiple clouds with a consistent platform.

- Go ServerlessFully managed environment for developing, deploying and scaling apps.

- Artificial IntelligenceAdd intelligence and efficiency to your business with AI and machine learning.

- Customer Engagement Suite with Google AIEnd-to-end application that combines our most advanced conversational AI.

- Document AIDocument processing and data capture automated at scale.

- Vertex AI Search for commerceGoogle-quality search and product recommendations for retailers.

- Google Cloud with GeminiAI assistants for application development, coding, and more.

- Generative AI on Google CloudTransform content creation and discovery, research, customer service, and developer efficiency with the power of generative AI.

- APIs and ApplicationsSpeed up the pace of innovation without coding, using APIs, apps, and automation.

- New Business Channels Using APIsAttract and empower an ecosystem of developers and partners.

- Unlocking Legacy Applications Using APIsCloud services for extending and modernizing legacy apps.

- Open Banking APIxSimplify and accelerate secure delivery of open banking compliant APIs.

- Data AnalyticsGenerate instant insights from data at any scale with a serverless, fully managed analytics platform that significantly simplifies analytics.

- Data MigrationMigrate and modernize your data warehouse and data lakes with AI-powered migration services.

- Data LakehouseUnify and govern your multimodal data with a high-performance and open data lakehouse.

- Real-time AnalyticsInsights from ingesting, processing, and analyzing event streams.

- Marketing AnalyticsSolutions for collecting, analyzing, and activating customer data.

- DatasetsData from Google, public, and commercial providers to enrich your analytics and AI initiatives.

- Business IntelligenceSolutions for modernizing your BI stack and creating rich data experiences.

- AI for Data AnalyticsWrite SQL, build predictive models, and visualize data with AI for data analytics.

- Geospatial AnalyticsA comprehensive platform to solve for geospatial use cases at scale.

- DatabasesMigrate and manage enterprise data with security, reliability, high availability, and fully managed data services.

- Database MigrationGuides and tools to simplify your database migration life cycle.

- Database ModernizationUpgrades to modernize your operational database infrastructure.

- Databases for GamesBuild global, live games with Google Cloud databases.

- Google Cloud DatabasesDatabase services to migrate, manage, and modernize data.

- Migrate Oracle workloads to Google CloudRehost, replatform, rewrite your Oracle workloads.

- Open Source DatabasesFully managed open source databases with enterprise-grade support.

- SQL Server on Google CloudOptions for running SQL Server virtual machines on Google Cloud.

- Gemini for DatabasesSupercharge database development and management with AI.

- Infrastructure ModernizationMigrate quickly with solutions for SAP, VMware, Windows, Oracle, and other workloads.

- Application MigrationDiscovery and analysis tools for moving to the cloud.

- SAP on Google CloudCertifications for running SAP applications and SAP HANA.

- High Performance ComputingCompute, storage, and networking options to support any workload.

- Windows on Google CloudTools and partners for running Windows workloads.

- Data Center MigrationMigration solutions for VMs, apps, databases, and more.

- Active AssistAutomatic cloud resource optimization and increased security.

- Virtual DesktopsRemote work solutions for desktops and applications (VDI & DaaS).

- Rapid Migration and Modernization ProgramEnd-to-end migration program to simplify your path to the cloud.

- Backup and Disaster RecoveryEnsure your business continuity needs are met.

- Red Hat on Google CloudGoogle and Red Hat provide an enterprise-grade platform for traditional on-prem and custom applications.

- Cross-Cloud NetworkSimplify hybrid and multicloud networking, and secure your workloads, data, and users.

- ObservabilityMonitor, troubleshoot, and improve app performance with end-to-end visibility.

- Productivity and CollaborationChange the way teams work with solutions designed for humans and built for impact.

- Google WorkspaceCollaboration and productivity tools for enterprises.

- Google Workspace EssentialsSecure video meetings and modern collaboration for teams.

- Cloud IdentityUnified platform for IT admins to manage user devices and apps.

- Chrome EnterpriseChromeOS, Chrome Browser, and Chrome devices built for business.

- SecurityDetect, investigate, and respond to online threats to help protect your business.

- Agentic SOCDelivering better security outcomes with AI agents.

- Web App and API ProtectionThreat and fraud protection for your web applications and APIs.

- Security and Resilience FrameworkSolutions for each phase of the security and resilience life cycle.

- Risk and compliance as code (RCaC)Solution to modernize your governance, risk, and compliance function with automation.

- Software Supply Chain SecuritySolution for improving end-to-end software supply chain security.

- Security FoundationRecommended products to help achieve a strong security posture.

- Google Cloud Cybershield™Strengthen nationwide cyber defense.

- Startups and SMBAccelerate startup and SMB growth with tailored solutions and programs.

- Startup ProgramGet financial, business, and technical support to take your startup to the next level.

- Small and Medium BusinessExplore solutions for web hosting, app development, AI, and analytics.

- Software as a ServiceBuild better SaaS products, scale efficiently, and grow your business.

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

- Compute EngineVirtual machines running in Google’s data center.

- Cloud StorageObject storage that’s secure, durable, and scalable.

- BigQueryAutonomous data to AI platform for analytics and data science.

- Cloud RunFully managed environment for running containerized apps.

- Google Kubernetes EngineManaged environment for running containerized apps.

- Agent PlatformUnified platform for ML models, generative AI, and agent building.

- LookerPlatform for BI, data applications, and embedded analytics.

- Apigee API ManagementManage the full life cycle of APIs anywhere with visibility and control.

- Cloud SQLRelational database services for MySQL, PostgreSQL and SQL Server.

- Gemini Enterprise appSecure platform to discover, create, run, and govern AI agents for employees.

- Cloud CDNContent delivery network for delivering web and video.

- Not seeing what you're looking for?

- See all products (100+)

- AI and Machine Learning

- Vertex AI PlatformUnified platform for ML models and generative AI.

- Vertex AI StudioBuild, tune, and deploy foundation models on Vertex AI.

- Vertex AI Agent BuilderBuild and deploy gen AI experiences.

- Conversational AgentsBuild conversational AI with both deterministic and gen AI functionality.

- Vertex AI SearchBuild Google-quality search for your enterprise apps and experiences.

- Speech-to-TextSpeech recognition and transcription across 125 languages.

- Text-to-SpeechSpeech synthesis in 220+ voices and 40+ languages.

- Translation AILanguage detection, translation, and glossary support.

- Gemini EnterpriseSecure platform to discover, create, run, and govern AI agents.

- Vision AICustom and pre-trained models to detect emotion, text, and more.

- Contact Center as a ServiceOmnichannel contact center solution that is native to the cloud.

- Not seeing what you're looking for?

- See all AI and machine learning products

- Business Intelligence

- LookerPlatform for BI, data applications, and embedded analytics.

- Looker StudioInteractive data suite for dashboarding, reporting, and analytics.

- Compute

- Compute EngineVirtual machines running in Google’s data center.

- App EngineServerless application platform for apps and back ends.

- Cloud GPUsGPUs for ML, scientific computing, and 3D visualization.

- Migrate to Virtual MachinesServer and virtual machine migration to Compute Engine.

- Spot VMsCompute instances for batch jobs and fault-tolerant workloads.

- BatchFully managed service for scheduling batch jobs.

- Sole-Tenant NodesDedicated hardware for compliance, licensing, and management.

- Bare MetalInfrastructure to run specialized workloads on Google Cloud.

- RecommenderUsage recommendations for Google Cloud products and services.

- VMware EngineFully managed, native VMware Cloud Foundation software stack.

- Cloud RunFully managed environment for running containerized apps.

- Not seeing what you're looking for?

- See all compute products

- Containers

- Google Kubernetes EngineManaged environment for running containerized apps.

- Cloud RunFully managed environment for running containerized apps.

- Cloud BuildSolution for running build steps in a Docker container.

- Artifact RegistryPackage manager for build artifacts and dependencies.

- Cloud CodeIDE support to write, run, and debug Kubernetes applications.

- Cloud DeployFully managed continuous delivery to GKE and Cloud Run.

- Migrate to ContainersComponents for migrating VMs into system containers on GKE.

- Deep Learning ContainersContainers with data science frameworks, libraries, and tools.

- KnativeComponents to create Kubernetes-native cloud-based software.

- Data Analytics

- BigQueryAutonomous data to AI platform for analytics and data science.

- LookerPlatform for BI, data applications, and embedded analytics.

- DataflowReal-time analytics for stream and batch processing.

- Pub/SubMessaging service for event ingestion and delivery.

- DataprocManaged service for running Apache Spark and Apache Hadoop clusters.

- Google Cloud Serverless for Apache SparkQuick VM startup and dynamic autoscaling for Spark workloads.

- Cloud ComposerWorkflow orchestration service built on Apache Airflow.

- BigLakeStorage engine for building data lakehouses with Apache Iceberg.

- Dataplex Universal CatalogA unified data-to-AI governance fabric for all Google Cloud services.

- BigQuery Migration ServicesFree-to-use, cloud-native and AI-powered data migration services.

- Managed Service for Apache KafkaManaged Kafka service to operate highly available Apache Kafka clusters.

- Not seeing what you're looking for?

- See all data analytics products

- Databases

- AlloyDB for PostgreSQLFully managed, PostgreSQL-compatible database for enterprise workloads.

- Cloud SQLFully managed database for MySQL, PostgreSQL, and SQL Server.

- FirestoreHighly scalable and serverless NoSQL document database, with MongoDB compatibility.

- SpannerCloud-native relational database with unlimited scale and 99.999% availability.

- BigtableCloud-native wide-column database for large-scale, low-latency workloads.

- DatastreamServerless change data capture and replication service.

- Database Migration ServiceServerless, minimal downtime migrations to Cloud SQL.

- Bare Metal SolutionFully managed infrastructure for your Oracle workloads.

- MemorystoreFully managed Redis and Memcached for sub-millisecond data access.

- Developer Tools

- Artifact RegistryUniversal package manager for build artifacts and dependencies.

- Cloud CodeIDE support to write, run, and debug Kubernetes applications.

- Cloud BuildContinuous integration and continuous delivery platform.

- Cloud DeployFully managed continuous delivery to GKE and Cloud Run.

- Cloud Deployment ManagerService for creating and managing Google Cloud resources.

- Cloud SDKCommand-line tools and libraries for Google Cloud.

- Cloud SchedulerCron job scheduler for task automation and management.

- Cloud Source RepositoriesPrivate Git repository to store, manage, and track code.

- Infrastructure ManagerAutomate infrastructure management with Terraform.

- Cloud WorkstationsManaged and secure development environments in the cloud.

- Gemini Code AssistAI-powered assistant available across Google Cloud and your IDE.

- Not seeing what you're looking for?

- See all developer tools

- Distributed Cloud

- Google Distributed Cloud ConnectedDistributed cloud services for edge workloads.

- Google Distributed Cloud Air-gappedDistributed cloud for air-gapped workloads.

- Hybrid and Multicloud

- Google Kubernetes EngineManaged environment for running containerized apps.

- Apigee API ManagementAPI management, development, and security platform.

- Migrate to ContainersTool to move workloads and existing applications to GKE.

- Cloud BuildService for executing builds on Google Cloud infrastructure.

- ObservabilityMonitoring, logging, and application performance suite.

- Cloud Service MeshFully managed service mesh based on Envoy and Istio.

- Google Distributed CloudFully managed solutions for the edge and data centers.

- Industry Specific

- Anti Money Laundering AIDetect suspicious, potential money laundering activity with AI.

- Cloud Healthcare APISolution for bridging existing care systems and apps on Google Cloud.

- Device Connect for FitbitGain a 360-degree patient view with connected Fitbit data on Google Cloud.

- Telecom Network AutomationReady to use cloud-native automation for telecom networks.

- Telecom Data FabricTelecom data management and analytics with an automated approach.

- Telecom Subscriber InsightsIngests data to improve subscriber acquisition and retention.

- Spectrum Access System (SAS)Controls fundamental access to the Citizens Broadband Radio Service (CBRS).

- Integration Services

- Application IntegrationConnect to 3rd party apps and enable data consistency without code.

- WorkflowsWorkflow orchestration for serverless products and API services.

- Apigee API ManagementManage the full life cycle of APIs anywhere with visibility and control.

- Cloud TasksTask management service for asynchronous task execution.

- Cloud SchedulerCron job scheduler for task automation and management.

- DataprocService for running Apache Spark and Apache Hadoop clusters.

- Cloud Data FusionData integration for building and managing data pipelines.

- Cloud ComposerWorkflow orchestration service built on Apache Airflow.

- Pub/SubMessaging service for event ingestion and delivery.

- EventarcBuild an event-driven architecture that can connect any service.

- Management Tools

- Cloud ShellInteractive shell environment with a built-in command line.

- Cloud consoleWeb-based interface for managing and monitoring cloud apps.

- Cloud EndpointsDeployment and development management for APIs on Google Cloud.

- Cloud IAMPermissions management system for Google Cloud resources.

- Cloud APIsProgrammatic interfaces for  Google Cloud services.

- Service CatalogService catalog for admins managing internal enterprise solutions.

- Cost ManagementTools for monitoring, controlling, and optimizing your costs.

- ObservabilityMonitoring, logging, and application performance suite.

- Carbon FootprintDashboard to view and export Google Cloud carbon emissions reports.

- Config ConnectorKubernetes add-on for managing Google Cloud resources.

- Active AssistTools for easily managing performance, security, and cost.

- Not seeing what you're looking for?

- See all management tools

- Maps and Geospatial

- Earth EngineGeospatial platform for Earth observation data and analysis.

- Google Maps PlatformCreate immersive location experiences and improve business operations.

- Media Services

- Cloud CDNContent delivery network for serving web and video content.

- Live Stream APIService to convert live video and package for streaming.

- OpenCueOpen source render manager for visual effects and animation.

- Transcoder APIConvert video files and package them for optimized delivery.

- Video Stitcher APIService for dynamic or server side ad insertion.

- Migration

- Migration CenterUnified platform for migrating and modernizing with Google Cloud.

- Application MigrationApp migration to the cloud for low-cost refresh cycles.

- Migrate to Virtual MachinesComponents for migrating VMs and physical servers to Compute Engine.

- Cloud Foundation ToolkitReference templates for Deployment Manager and Terraform.

- Database Migration ServiceServerless, minimal downtime migrations to Cloud SQL.

- Migrate to ContainersComponents for migrating VMs into system containers on GKE.

- BigQuery Migration ServicesStreamlined data warehouse and data lake migration tooling and incentives.

- Rapid Migration and Modernization ProgramEnd-to-end migration program to simplify your path to the cloud.

- Transfer ApplianceStorage server for moving large volumes of data to Google Cloud.

- Storage Transfer ServiceData transfers from online and on-premises sources to Cloud Storage.

- VMware EngineMigrate and run your VMware workloads natively on Google Cloud.

- Networking

- Cloud ArmorSecurity policies and defense against web and DDoS attacks.

- Cloud CDN and Media CDNContent delivery network for serving web and video content.

- Cloud DNSDomain name system for reliable and low-latency name lookups.

- Cloud Load BalancingService for distributing traffic across applications and regions.

- Cloud NATNAT service for giving private instances internet access.

- Cloud ConnectivityConnectivity options for VPN, peering, and enterprise needs.

- Network Connectivity CenterConnectivity management to help simplify and scale networks.

- Network Intelligence CenterNetwork monitoring, verification, and optimization platform.

- Network Service TiersCloud network options  based on performance, availability, and cost.

- Virtual Private CloudSingle VPC for an entire organization, isolated within projects.

- Private Service ConnectSecure connection between your VPC and services.

- Not seeing what you're looking for?

- See all networking products

- Operations

- Cloud LoggingGoogle Cloud audit, platform, and application logs management.

- Cloud MonitoringInfrastructure and application health with rich metrics.

- Error ReportingApplication error identification and analysis.

- Managed Service for PrometheusFully-managed Prometheus on Google Cloud.

- Cloud TraceTracing system collecting latency data from applications.

- Cloud ProfilerCPU and heap profiler for analyzing application performance.

- Cloud QuotasManage quotas for all Google Cloud services.

- Productivity and Collaboration

- AppSheetNo-code development platform to build and extend applications.

- Gemini EnterpriseSecure platform to discover, create, run, and govern AI agents.

- Google WorkspaceCollaboration and productivity tools for individuals and organizations.

- Google Workspace EssentialsSecure video meetings and modern collaboration for teams.

- Cloud IdentityUnified platform for IT admins to manage user devices and apps.

- Chrome EnterpriseChromeOS, Chrome browser, and Chrome devices built for business.

- Security and Identity

- Cloud IAMPermissions management system for Google Cloud resources.

- Sensitive Data ProtectionDiscover, classify, and protect your valuable data assets.

- Mandiant Managed DefenseFind and eliminate threats with confidence 24x7.

- Google Threat IntelligenceKnow who’s targeting you.

- Security Command CenterPlatform for defending against threats to your Google Cloud assets.

- Cloud Key ManagementManage encryption keys on Google Cloud.

- Mandiant Incident ResponseMinimize the impact of a breach.

- Chrome Enterprise PremiumGet secure enterprise browsing with extensive endpoint visibility.

- Assured WorkloadsCompliance and security controls for sensitive workloads.

- Google Security OperationsDetect, investigate, and respond to cyber threats.

- Mandiant ConsultingGet expert guidance before, during, and after an incident.

- Not seeing what you're looking for?

- See all security and identity products

- Serverless

- Cloud RunFully managed environment for running containerized apps.

- Cloud FunctionsPlatform for creating functions that respond to cloud events.

- App EngineServerless application platform for apps and back ends.

- WorkflowsWorkflow orchestration for serverless products and API services.

- API GatewayDevelop, deploy, secure, and manage APIs with a fully managed gateway.

- Storage

- Cloud StorageObject storage that’s secure, durable, and scalable.

- Block StorageHigh-performance storage for AI, analytics, databases, and enterprise applications.

- FilestoreFile storage that is highly scalable and secure.

- Persistent DiskBlock storage for virtual machine instances running on Google Cloud.

- Cloud Storage for FirebaseObject storage for storing and serving user-generated content.

- Local SSDBlock storage that is locally attached for high-performance needs.

- Storage Transfer ServiceData transfers from online and on-premises sources to Cloud Storage.

- Google Cloud Managed LustreHigh performance managed parallel file service.

- Google Cloud NetApp VolumesFile storage service for NFS, SMB, and multi-protocol environments.

- Backup and DR ServiceService for centralized, application-consistent data protection.

- Web3

- Blockchain Node EngineFully managed node hosting for developing on the blockchain.

- Blockchain RPCEnterprise-grade RPC for building on the blockchain.

- Save money with our transparent approach to pricing

- Google Cloud's pay-as-you-go pricing offers automatic savings based on monthly usage and discounted rates for prepaid resources. Contact us today to get a quote.

- Request a quote

- Pricing overview and tools

- Google Cloud pricingPay only for what you use with no lock-in.

- Pricing calculatorCalculate your cloud savings.

- Google Cloud free tierExplore products with free monthly usage.

- Cost optimization frameworkGet best practices to optimize workload costs.

- Cost management toolsTools to monitor and control your costs.

- Product-specific Pricing

- Compute Engine

- Cloud SQL

- Google Kubernetes Engine

- Cloud Storage

- BigQuery

- See full price list with 100+ products

- Learn & build

- Google Cloud Free Program$300 in free credits and 20+ free products.

- Solution GeneratorGet AI generated solution recommendations.

- QuickstartsGet tutorials and walkthroughs.

- BlogRead our latest product news and stories.

- Learning HubGrow your career with role-based training.

- Google Cloud certificationPrepare and register for certifications.

- Cloud computing basicsLearn more about cloud computing basics.

- Cloud Architecture CenterGet reference architectures and best practices.

- Connect

- InnovatorsJoin Google Cloud's developer program.

- Developer CenterStay in the know and stay connected.

- Events and webinarsBrowse upcoming and on demand events.

- Google Cloud CommunityAsk questions, find answers, and connect.

- Consulting and Partners

- Google Cloud ConsultingWork with our experts on cloud projects.

- Google Cloud MarketplaceDeploy ready-to-go solutions in a few clicks.

- Find a partnerExplore the benefits of working with a partner.

- Google Cloud partnersLearn about the ecosystem and resources.

- Overviewarrow_forward

- Solutionsarrow_forward

- Productsarrow_forward

- Pricingarrow_forward

- Resourcesarrow_forward

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

- Vertex AI Platform

- Vertex AI Studio

- Vertex AI Agent Builder

- Conversational Agents

- Vertex AI Search

- Speech-to-Text

- Text-to-Speech

- Translation AI

- Gemini Enterprise

- Vision AI

- Contact Center as a Service

- See all AI and machine learning products

- Business Intelligence

- Looker

- Looker Studio

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

- Looker

- Dataflow

- Pub/Sub

- Dataproc

- Google Cloud Serverless for Apache Spark

- Cloud Composer

- BigLake

- Dataplex Universal Catalog

- BigQuery Migration Services

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

- Why GoogleChoosing Google CloudTrust and securityModern Infrastructure CloudMulticloudGlobal infrastructureLocationsCustomers and case studiesAnalyst reportsWhitepapersBlog

## Why Google

- Choosing Google Cloud

- Trust and security

- Modern Infrastructure Cloud

- Multicloud

- Global infrastructure

- Locations

- Customers and case studies

- Analyst reports

- Whitepapers

- Blog

- Products and pricingGoogle Cloud pricingGoogle Workspace pricingSee all products

## Products and pricing

- Google Cloud pricing

- Google Workspace pricing

- See all products

- SolutionsInfrastructure modernizationDatabasesApplication modernizationSmart analyticsArtificial IntelligenceSecurityProductivity & work transformationIndustry solutionsDevOps solutionsSmall business solutionsSee all solutions

## Solutions

- Infrastructure modernization

- Databases

- Application modernization

- Smart analytics

- Artificial Intelligence

- Security

- Productivity & work transformation

- Industry solutions

- DevOps solutions

- Small business solutions

- See all solutions

- ResourcesGoogle Cloud Affiliate ProgramGoogle Cloud documentationGoogle Cloud quickstartsGoogle Cloud MarketplaceLearn about cloud computingSupportCode samplesCloud Architecture CenterTrainingCertificationsGoogle for DevelopersGoogle Cloud for StartupsSystem statusRelease Notes

## Resources

- Google Cloud Affiliate Program

- Google Cloud documentation

- Google Cloud quickstarts

- Google Cloud Marketplace

- Learn about cloud computing

- Support

- Code samples

- Cloud Architecture Center

- Training

- Certifications

- Google for Developers

- Google Cloud for Startups

- System status

- Release Notes

- EngageContact salesFind a PartnerBecome a PartnerEventsPodcastsDeveloper CenterPress CornerGoogle Cloud on YouTubeGoogle Cloud Tech on YouTubeFollow on XJoin User ResearchWe're hiring. Join Google Cloud!Community forums

## Engage

- Contact sales

- Find a Partner

- Become a Partner

- Events

- Podcasts

- Developer Center

- Press Corner

- Google Cloud on YouTube

- Google Cloud Tech on YouTube

- Follow on X

- Join User Research

- We're hiring. Join Google Cloud!

- Community forums

- About Google

- Privacy

- Site terms

- Google Cloud terms

- Cookies management controls

- Our third decade of climate action: join us

- Sign up for the Google Cloud newsletterSubscribe

- ‪English‬

- ‪Deutsch‬

- ‪Español‬

- ‪Español (Latinoamérica)‬

- ‪Français‬

- ‪Indonesia‬

- ‪Italiano‬

- ‪Português (Brasil)‬

- ‪简体中文‬

- ‪繁體中文‬

- ‪日本語‬

- ‪한국어‬
