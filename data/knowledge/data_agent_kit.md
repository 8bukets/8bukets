# The future of agentic development: Redefining the data practitioner lifecycle with Data Agent Kit
May 20, 2026

**Brahm Kohli**, Group Product Manager, Data Cloud
**Dinesh Chandnani**, Director of Engineering, Data Cloud

The modern software development landscape isn’t happening just on one surface — it’s happening across an entire ecosystem of agentic tools. Agents are being developed at an unprecedented scale, and these agents require direct access to enterprise data for context and grounding.

However, the current tooling for building agents and managing data is heavily fragmented. This can make it difficult to access data, increasing security risks, and causing broken developer experiences that hinder innovation.

To address this challenge, we recently launched Data Agent Kit, a unified, open-source collection of data engineering and data science skills, tools and plugins that integrate directly into the environments practitioners already use, such as VS Code, Claude Code, Codex, Gemini CLI and the Antigravity CLI. By seamlessly bringing together these core tools and skills with your enterprise data, the Data Agent Kit effectively serves as a comprehensive harness for agentic context, memory, and personalization. It provides:

* **Agentic skills:** Pre-codified pathways for interacting with your data estate, covering query optimization, ML best practices, data validation, data drift checks, governance, and troubleshooting.
* **Model Context Protocol (MCP) tools:** Secure connections between agentic workflows and cloud data platforms like BigQuery, AlloyDB, and Google Cloud Storage. Developers can now configure connection parameters for their cloud datasets and data processing engines without having to manage complex, manual pipeline code.
* **Plugins and extensions:** Native IDE integrations that enable rich, context-aware developer interactions.

Together, these Data Agent Kit capabilities help data practitioners go from manually writing code to intent-driven data science and engineering: defining the desired business outcomes, constraints, and success criteria, and allowing the AI-augmented system to figure out how to execute it. This shift is critical because today, when building agentic applications that navigate complex data architectures, there’s often a 'context window tax' i.e., developers have to manually paste vast amounts of schema metadata into prompts, eating up token limits and increasing latency. Meanwhile, data practitioners often lack guidance about how to efficiently query, optimize, and troubleshoot cloud data, while specialized, fragmented development environments cannot see across your entire data estate. Data Agent Kit helps with these challenges and others, providing the foundational capabilities data practitioners need for a new agentic way of working.

Read on for an overview of Data Agent Kit’s features and benefits, how to install it and connect your local environment to your data estate, and an intent-driven engineering example.

## A unified hub for your data estate and lifecycle

Data Agent Kit makes your entire data estate available in a single view. This goes beyond providing a simple catalog for databases such as BigQuery, AlloyDB and Spanner; rather, it integrates data engineering and science tasks, orchestration pipelines, and jobs into a single interface. This allows practitioners to manage their entire data workflow — from discovery to production — without context switching. Data Agent Kit’s intelligent routing automatically chooses the optimal compute engine for your task — whether that’s BigQuery for SQL-native analytics and ELT, or Spark for custom Python transformations and distributed ML training.

![Unified Catalog](https://storage.googleapis.com/gweb-cloudblog-publish/original_images/1_Unified_Catalog.gif)
*Unified Hub of your entire data estate and lifecycle*

## Ecosystem-led intelligence: Codified agentic skills

Data Agent Kit offers a library of predefined agentic skills (e.g., ML best practices, ELT, building data apps) based on Google Cloud’s data engineering and science expertise. Rather than relying on generic LLM prompts, it codifies prescriptive guidelines into your workflow. This allows you to inject enterprise-grade data intelligence directly into your IDE or CLI.

![Agentic Skills](https://storage.googleapis.com/gweb-cloudblog-publish/original_images/2_Agentic_Skills.gif)
*Browsing a predefined list of agentic data engineering and science skills*

## Transforming data exploration through natural language

Grounded in this unified data, Data Agent Kit delivers native conversational analytics directly within your workspace, making it easy to explore your data. Powered by the same Gemini natural language to SQL technology found in our first-party agents (e.g., Conversational BigQuery and Looker), Data Agent Kit lets you run natural language queries to profile, search, and visualize your datasets.

![Conversational Analytics](https://storage.googleapis.com/gweb-cloudblog-publish/original_images/3_Conversational_Analytics.gif)
*Within Data Agent Kit, you can use Conversational Analytics to explore your data*

## A practical walkthrough: Unifying data and building models

To see how Data Agent Kit’s skills and MCP tools work together, consider a financial services scenario: Your company is facing rising fraud claims. With your transaction data stored in Cloud Storage, you need to build a high-confidence fraud detection model and schedule orchestration pipelines. Traditionally, this involves hours of data wrangling across multiple consoles. With the Data Agent Kit, you can complete this in minutes, directly within your IDE or CLI. Let’s see how.

### Onboarding: The one-minute setup

You can get started with the Data Agent Kit in under a minute through an integrated setup process.
To do so, search for "Google Cloud Data Agent Kit" in your IDE’s marketplace (VS Code) or via the GitHub repo in your CLI (Gemini, Antigravity, Claude, Codex) from the links in the “Get started today” section below. Data Agent Kit automatically configures dependencies and checks your Google Cloud login status.

![VS Code Marketplace Extension](https://storage.googleapis.com/gweb-cloudblog-publish/images/4_VS_Code_Marketplace_Extension.max-900x900.jpg)

Click the Google Cloud icon in your activity bar to authenticate via IAM. Once logged in, your Cloud Storage, databases, and catalog assets appear instantly in your workspace.
Use the settings menu to set project IDs, regions, and verify MCP status to ensure all backend services are authorized. Data Agent Kit also includes a quick-start guide on using the tools and skills.

![Data Agent Kit Extension Installed](https://storage.googleapis.com/gweb-cloudblog-publish/images/5_Data_Agent_Kit_Extension_Installed.max-1400x1400.jpg)

### An intent-driven data engineering example

With Data Agent Kit installed, you can skip the manual ETL boilerplate, and directly describe your high-level goal to your coding assistant (e.g., Claude Code, GitHub Copilot) in natural language. The assistant leverages Data Agent Kit’s skills to plan and execute the workflow.

**Prompt:**
> I have the raw transaction logs landing in the GCS bucket gs://fin-clearing-raw/.
> First, create a Spark notebook and (1) ingest these logs into an Iceberg table in BigQuery.
> Second, create a dbt project to (2) deduplicate them, (3) remove the transactions with invalid transaction id and store them in a separate Iceberg table, (4) standardize the timestamps and perform any other necessary cleanup tasks (5) sync the output to another Iceberg table (6) join this output table with tables that have payer and payees identities and write the output to a final Iceberg table.
> Third, I would like you to train an ML model on Spark using a notebook to detect fraudulent transactions in the output table. I am thinking about a LightGBM model but I am open to any suggestions you might have. Use the relevant datasets in the project.
> Finally, create an inferencing step using Spark notebook to the above pipeline to perform batch inferencing and write flagged transactions to a Spanner table.
> Create an orchestration pipeline that first runs the ingestion then the dbt and next the inference notebook.

### Under the hood: Data pipeline steps

Behind the scenes, Data Agent Kit plans a robust multi-step orchestration of the entire data lifecycle, from exploration to inference.

**Step 1: Notebook creation, ingestion and initial storage**
Find your bronze data — raw, unfiltered data on financial transactions — and bring it into an Iceberg table before doing the transformations.
*   Automatically create a Notebook to ingest the raw logs from Cloud Storage.
*   Write the necessary SQL, and store the ingested data into an Iceberg table in BigQuery.

![Ingestion](https://storage.googleapis.com/gweb-cloudblog-publish/original_images/6_Ingestion.gif)
*Ingestion into a bronze table*

**Step 2: Transformation (dbt Project)**
Now, clean the bronze data into silver and gold tables:
*   Data preparation: Deduplicate the transaction logs.
*   Filter invalid IDs: Identify transactions with invalid IDs and store them in a separate Iceberg table.
*   Clean and standardize: Standardize timestamps and perform other necessary cleanup tasks.
*   Sync: Output the cleaned data to another Iceberg table, leveraging the BigQuery MCP server.
*   Enrichment: Join the cleaned table with payer and payee identity tables.
*   Final output: Write the joined dataset to a final Iceberg table.

![Transformation](https://storage.googleapis.com/gweb-cloudblog-publish/original_images/7_Transformation.gif)
*Data transformation to create silver and gold tables*

**Step 3: Machine learning and inferencing**
With your gold table minted, it’s time for some data science: model training and inferencing. Here, the agent hands the clean data from the previous step to the model to spot fraudulent patterns.
*   Training: Use a Spark notebook to train an ML model.
*   Inference: Create a Spark notebook inferencing step for batch processing.
*   Storage: Write all flagged fraudulent transactions to a Spanner table by leveraging the Spanner MCP.

![ML Inferencing](https://storage.googleapis.com/gweb-cloudblog-publish/original_images/8_ML_Inferencing.gif)
*Machine learning and inference*

**Step 4: Orchestration and execution**
Finally, you’re ready to move to production and schedule the whole orchestration pipeline: Ingestion -> Transformation -> Inference.

![Orchestration](https://storage.googleapis.com/gweb-cloudblog-publish/original_images/9_Orchestration.gif)
*Orchestration pipelines and scheduling runs*

### When things go sideways: Agentic incident management and intelligent recovery

If an orchestration pipeline fails, not to worry, Data Agent Kit streamlines resolution using its intelligent incident management capabilities:
*   Intelligent diagnosis: Automatically conducts root cause analysis to pinpoint failure sources
*   Autonomous remediation: Drafts and tests fixes, bypassing manual debugging
*   Automated recovery: Validates and deploys fixes via automated Git workflows

![Issue diagnosis and remediation](https://storage.googleapis.com/gweb-cloudblog-publish/original_images/10_Issue_diagnosis_and_remediation.gif)
*Issue diagnosis and remediation*

And there you have it: You’ve gone from raw discovery to a fully automated, fraud-catching machine in a matter of minutes, all from within the same UX. No need to hop between multiple browser tabs, IDE interfaces, or learn data engineering and science best practices — Data Agent Kit orchestrates a clean end-to-end flow leveraging various MCP tools and codified skills. Ultimately, this approach helps you achieve what matters most: shipping innovative, high-performance data applications at scale.
