# ANTIGRAVITY AI AGENTS KNOWLEDGE BASE

*Last Updated: 2026-05-23T11:14:58.238Z*

## DOCUMENT: Docker | Terraform | HashiCorp DeveloperInteractive
**Source:** https://developer.hashicorp.com/terraform/tutorials/docker-get-started
**Ingested At:** 2026-05-23T11:14:53.693Z

### Introduction
[HashiConf 2025 Don't miss the live stream of HashiConf Day 2 happening now View live stream](https://www.hashicorp.com/conferences/hashiconf#livestream)
[All HCP Products](/hcp)
- Infrastructure Lifecycle ManagementTerraformManage infrastructure as codePackerBuild machine imagesNomadOrchestrate workloadsWaypointStandardize application patternsVagrantBuild developer environments
- TerraformManage infrastructure as code
[TerraformManage infrastructure as code](/terraform)
- PackerBuild machine images
[PackerBuild machine images](/packer)
- NomadOrchestrate workloads
[NomadOrchestrate workloads](/nomad)
- WaypointStandardize application patterns
[WaypointStandardize application patterns](/waypoint)
- VagrantBuild developer environments
[VagrantBuild developer environments](/vagrant)
- Security Lifecycle ManagementVaultCentrally manage secretsBoundarySecure remote accessVault RadarScan for embedded secretsConsulSecure network services
- VaultCentrally manage secrets
[VaultCentrally manage secrets](/vault)
- BoundarySecure remote access
[BoundarySecure remote access](/boundary)
- Vault RadarScan for embedded secrets
[Vault RadarScan for embedded secrets](/hcp/docs/vault-radar)
- ConsulSecure network services
[ConsulSecure network services](/consul)
- CertificationsGet HashiCorp certified
[CertificationsGet HashiCorp certified](/certifications)
- TutorialsLearn HashiCorp products
[TutorialsLearn HashiCorp products](/tutorials)
- Validated PatternsField-tested patterns for using HashiCorp products
[Validated PatternsField-tested patterns for using HashiCorp products](/validated-patterns)
- Well-Architected FrameworkAdopt HashiCorp best practices
[Well-Architected FrameworkAdopt HashiCorp best practices](/well-architected-framework)
[Terraform](/terraform)
- Install
[Install](/terraform/install)
- Tutorials
[Tutorials](/terraform/tutorials)
- DocumentationDocumentationIntro to TerraformConfiguration LanguageTerraform CLIHCP TerraformTerraform EnterpriseTerraform MCP ServerBETATerraform MigrateProvider UsePlugin DevelopmentRegistry PublishingIntegration Program
- Documentation
[Documentation](/terraform/docs)
- Intro to Terraform
[Intro to Terraform](/terraform/intro)
- Configuration Language
[Configuration Language](/terraform/language)
- Terraform CLI
[Terraform CLI](/terraform/cli)
- HCP Terraform
[HCP Terraform](/terraform/cloud-docs)
- Terraform Enterprise
[Terraform Enterprise](/terraform/enterprise)
- Terraform MCP ServerBETA
[Terraform MCP ServerBETA](/terraform/mcp-server)
- Terraform Migrate
[Terraform Migrate](/terraform/migrate)
- Provider Use
[Provider Use](/terraform/language/providers)
- Plugin Development
[Plugin Development](/terraform/plugin)
- Registry Publishing
[Registry Publishing](/terraform/registry)
- Integration Program
[Integration Program](/terraform/docs/partnerships)
- Sandbox
- Registry(opens in new tab)
[Registry](https://registry.terraform.io/)
- Try Cloud(opens in new tab)
[Try Cloud](https://app.terraform.io/public/signup/account)
- Sign in
- Sign up
[Sign up](/sign-up)
- Theme
[Terraform Home](/terraform)

### Tutorials
[Tutorials](/terraform/tutorials)

### - AWS
[AWS](/terraform/tutorials/aws-get-started)
- Azure
[Azure](/terraform/tutorials/azure-get-started)
- Docker
[Docker](/terraform/tutorials/docker-get-started)

### - GCP
[GCP](/terraform/tutorials/gcp-get-started)
- HCP Terraform
[HCP Terraform](/terraform/tutorials/cloud-get-started)

### - OCI
[OCI](/terraform/tutorials/oci-get-started)
- Sandbox
[Sandbox](/terraform/tutorials/sandbox)

### - CLI
[CLI](/terraform/tutorials/cli)
- Configuration Language
[Configuration Language](/terraform/tutorials/configuration-language)
- HCP Terraform
[HCP Terraform](/terraform/tutorials/cloud)
- Modules
[Modules](/terraform/tutorials/modules)
- Provision
[Provision](/terraform/tutorials/provision)
- State
[State](/terraform/tutorials/state)

### Use Cases
- Applications
[Applications](/terraform/tutorials/applications)
- AWS Services
[AWS Services](/terraform/tutorials/aws)
- Azure Services
[Azure Services](/terraform/tutorials/azure)
- HashiCorp Products
[HashiCorp Products](/terraform/tutorials/hashicorp)
- IT/SaaS Providers
[IT/SaaS Providers](/terraform/tutorials/it-saas)
- Kubernetes
[Kubernetes](/terraform/tutorials/kubernetes)
- Machine Images
[Machine Images](/terraform/tutorials/virtual-machine)
- Networking
[Networking](/terraform/tutorials/networking)
- Policy
[Policy](/terraform/tutorials/policy)
- Security
[Security](/terraform/tutorials/security)

### Certification Prep
- Associate Prep (004)
[Associate Prep (004)](/terraform/tutorials/certification-004)
- Professional Prep
[Professional Prep](/terraform/tutorials/pro-cert)

### Production
- Automate Terraform
[Automate Terraform](/terraform/tutorials/automation)
- Enterprise Patterns
[Enterprise Patterns](/terraform/tutorials/recommended-patterns)
- Terraform Enterprise
[Terraform Enterprise](/terraform/tutorials/enterprise)

### Integrations
- Community Providers
[Community Providers](/terraform/tutorials/community-providers)
- Custom Framework Providers
[Custom Framework Providers](/terraform/tutorials/providers-plugin-framework)
- Secrets
[Secrets](/terraform/tutorials/secrets)
- Resources

### Resources
- Tutorial Library
[Tutorial Library](/tutorials/library?product=terraform)
- Certifications
[Certifications](/certifications/infrastructure-automation)
- Sandbox
[Sandbox](/terraform/sandbox)
- Community Forum(opens in new tab)
[Community Forum](https://discuss.hashicorp.com/c/terraform-core/27)
- Support(opens in new tab)
[Support](https://www.ibm.com/mysupport)
- GitHub(opens in new tab)
[GitHub](https://github.com/hashicorp/terraform)
- Terraform Registry(opens in new tab)
[Terraform Registry](https://registry.terraform.io/)
- Developer
[Developer](/)
- Terraform
[Terraform](/terraform)
- Tutorials
[Tutorials](/terraform/tutorials)
- Docker

### Get Started - Docker
Build, change, and destroy Docker infrastructure using Terraform. Step-by-step, command-line tutorials will walk you through the Terraform basics for the first time.

[Start](/terraform/tutorials/docker-get-started/infrastructure-as-code)
- Interactive3minWhat is Infrastructure as Code with Terraform?Learn how infrastructure as code lets you safely build, change, and manage infrastructure. Try Terraform.TerraformVideo
- Terraform
- Video
- 7minInstall TerraformInstall Terraform on Mac, Linux, or Windows by downloading the binary or using a package manager (Homebrew or Chocolatey). Then create a Docker container locally by following a quick-start tutorial to check that Terraform installed correctly.TerraformVideo
- Terraform
- Video
- 10minBuild infrastructureUse Terraform to deploy a Docker container, format your Terraform configuration, and review your infrastructure state.Terraform
- Terraform
- 4minChange infrastructureModify Docker container configuration to use a different external port. Plan and apply the changes to re-provision a new container that reflects the new configuration. Learn how Terraform handles infrastructure change management.Terraform
- Terraform
- 2minDestroy infrastructureDestroy the Docker container you created in the previous tutorials. Evaluate the plan and confirm the destruction.Terraform
- Terraform
- 4minDefine input variablesDeclare your Docker container name as a variable. Reference the variable in Terraform configuration. Define variables using command line flags, environment variables, .tfvars files or default values.Terraform
- Terraform
- 5minQuery data with outputsDeclare output values to display a Docker containers name and ID. Display all outputs and query specific outputs. Define what data stored in Terraform state is relevant to the operator or end user.Terraform
- Terraform
- Certifications
[Certifications](/certifications)
- System Status
[System Status](https://status.hashicorp.com)
- Cookie Manager
- Terms of Use
[Terms of Use](https://www.hashicorp.com/terms-of-service)
- Security
[Security](https://www.hashicorp.com/trust/security)
- Privacy
[Privacy](https://www.hashicorp.com/privacy)
- Trademark Policy
[Trademark Policy](https://www.hashicorp.com/trademark-policy)
- Trade Controls
[Trade Controls](https://www.hashicorp.com/trade-controls)
- Accessibility
[Accessibility](https://www.hashicorp.com/trust/accessibility)
- Give Feedback(opens in new tab)
[Give Feedback](https://forms.gle/fnHLuNahLEhjuKvE6)
- stdin is not a tty

---

## DOCUMENT: Terraform | HashiCorp Developer
**Source:** https://developer.hashicorp.com/terraform
**Ingested At:** 2026-05-23T11:14:55.094Z

### Introduction
[HashiConf 2025 Don't miss the live stream of HashiConf Day 2 happening now View live stream](https://www.hashicorp.com/conferences/hashiconf#livestream)
[All HCP Products](/hcp)
- Infrastructure Lifecycle ManagementTerraformManage infrastructure as codePackerBuild machine imagesNomadOrchestrate workloadsWaypointStandardize application patternsVagrantBuild developer environments
- TerraformManage infrastructure as code
[TerraformManage infrastructure as code](/terraform)
- PackerBuild machine images
[PackerBuild machine images](/packer)
- NomadOrchestrate workloads
[NomadOrchestrate workloads](/nomad)
- WaypointStandardize application patterns
[WaypointStandardize application patterns](/waypoint)
- VagrantBuild developer environments
[VagrantBuild developer environments](/vagrant)
- Security Lifecycle ManagementVaultCentrally manage secretsBoundarySecure remote accessVault RadarScan for embedded secretsConsulSecure network services
- VaultCentrally manage secrets
[VaultCentrally manage secrets](/vault)
- BoundarySecure remote access
[BoundarySecure remote access](/boundary)
- Vault RadarScan for embedded secrets
[Vault RadarScan for embedded secrets](/hcp/docs/vault-radar)
- ConsulSecure network services
[ConsulSecure network services](/consul)
- CertificationsGet HashiCorp certified
[CertificationsGet HashiCorp certified](/certifications)
- TutorialsLearn HashiCorp products
[TutorialsLearn HashiCorp products](/tutorials)
- Validated PatternsField-tested patterns for using HashiCorp products
[Validated PatternsField-tested patterns for using HashiCorp products](/validated-patterns)
- Well-Architected FrameworkAdopt HashiCorp best practices
[Well-Architected FrameworkAdopt HashiCorp best practices](/well-architected-framework)
[Terraform](/terraform)
- Install
[Install](/terraform/install)
- Tutorials
[Tutorials](/terraform/tutorials)
- DocumentationDocumentationIntro to TerraformConfiguration LanguageTerraform CLIHCP TerraformTerraform EnterpriseTerraform MCP ServerBETATerraform MigrateProvider UsePlugin DevelopmentRegistry PublishingIntegration Program
- Documentation
[Documentation](/terraform/docs)
- Intro to Terraform
[Intro to Terraform](/terraform/intro)
- Configuration Language
[Configuration Language](/terraform/language)
- Terraform CLI
[Terraform CLI](/terraform/cli)
- HCP Terraform
[HCP Terraform](/terraform/cloud-docs)
- Terraform Enterprise
[Terraform Enterprise](/terraform/enterprise)
- Terraform MCP ServerBETA
[Terraform MCP ServerBETA](/terraform/mcp-server)
- Terraform Migrate
[Terraform Migrate](/terraform/migrate)
- Provider Use
[Provider Use](/terraform/language/providers)
- Plugin Development
[Plugin Development](/terraform/plugin)
- Registry Publishing
[Registry Publishing](/terraform/registry)
- Integration Program
[Integration Program](/terraform/docs/partnerships)
- Sandbox
- Registry(opens in new tab)
[Registry](https://registry.terraform.io/)
- Try Cloud(opens in new tab)
[Try Cloud](https://app.terraform.io/public/signup/account)
- Sign in
- Sign up
[Sign up](/sign-up)
- Theme

### Terraform
- Terraform
[Terraform](/terraform)
- Install
[Install](/terraform/install)
- Intro to Terraform
[Intro to Terraform](/terraform/intro)
- Tutorials
[Tutorials](/terraform/tutorials)
- DocumentationDocumentationConfiguration LanguageTerraform CLIHCP TerraformTerraform EnterpriseTerraform MCP ServerBETATerraform MigrateProvider UsePlugin DevelopmentRegistry PublishingIntegration Program
- Documentation
[Documentation](/terraform/docs)
- Configuration Language
[Configuration Language](/terraform/language)
- Terraform CLI
[Terraform CLI](/terraform/cli)
- HCP Terraform
[HCP Terraform](/terraform/cloud-docs)
- Terraform Enterprise
[Terraform Enterprise](/terraform/enterprise)
- Terraform MCP ServerBETA
[Terraform MCP ServerBETA](/terraform/mcp-server)
- Terraform Migrate
[Terraform Migrate](/terraform/migrate)
- Provider Use
[Provider Use](/terraform/language/providers)
- Plugin Development
[Plugin Development](/terraform/plugin)
- Registry Publishing
[Registry Publishing](/terraform/registry)
- Integration Program
[Integration Program](/terraform/docs/partnerships)
- Resources

### Resources
- Tutorial Library
[Tutorial Library](/tutorials/library?product=terraform)
- Certifications
[Certifications](/certifications/infrastructure-automation)
- Sandbox
[Sandbox](/terraform/sandbox)
- Community Forum(opens in new tab)
[Community Forum](https://discuss.hashicorp.com/c/terraform-core/27)
- Support(opens in new tab)
[Support](https://www.ibm.com/mysupport)
- GitHub(opens in new tab)
[GitHub](https://github.com/hashicorp/terraform)
- Terraform Registry(opens in new tab)
[Terraform Registry](https://registry.terraform.io/)
- Developer
[Developer](/)
- Terraform

### Automate Infrastructure on Any Cloud
- Install
- Tutorials
- Documentation

### What is Terraform?
Terraform is an infrastructure as code tool that lets you build, change, and version infrastructure safely and efficiently. This includes low-level components like compute instances, storage, and networking; and high-level components like DNS entries and SaaS features.

[Learn more](/terraform/intro)

### Get Started
Follow a code-complete, hands-on tutorial to learn the Terraform basics with your favorite infrastructure provider.

- Amazon Web Services
- Azure
- HCP Terraform
- Google Cloud Platform
- Oracle Cloud
- Docker

### Sandbox
- Terraform sandboxThe Terraform sandbox contains preinstalled tools and services for you to experiment with Terraform.

### Best Practices
- Terraform style guideLearn recommended style conventions for Terraform configuration and workflows.
- Phases of Terraform adoptionDesign your Terraform workflows for scale.

### Featured Documentation
- Configuration LanguageDescribe infrastructure in Terraform configuration language.
- Terraform CLILearn Terraform's CLI-based workflows.
- HCP TerraformCollaborate with your team to provision infrastructure.

### Popular Use Cases
- 25minDeploy federated multi-cloud Kubernetes clustersUse Terraform to provision Kubernetes clusters in the Azure and AWS clouds, deploy Consul Helm charts enabling Consul federation, and deploy an example application on both clusters.TerraformConsul
- Terraform
- Consul
- 25minCreate preview environments with Terraform, GitHub Actions, and VercelConfigure HCP Terraform and GitHub Actions to create frontend and backend preview environments for your application. Dynamically create and destroy preview environments by opening, merging and closing pull requests.Terraform
- Terraform
- 43minBuild a golden image pipeline with HCP PackerCreate a golden image pipeline with HCP Packer. Build an application image on the base with Packer and provision it on AWS with Terraform.TerraformPacker
- Terraform
- Packer

### Get Certified
- 3 tutorials Prepare for the Terraform Associate 004 Certification ExamPrepare for the Terraform Associate exam. Choose to follow an in-depth guide or to review select exam topics depending on the kind of preparation support you need. Then review sample questions to learn what to expect on exam day. Terraform
- Terraform
- 6 tutorials Prepare for the Terraform Authoring and Operations Professional Certification ExamPrepare for your Terraform Professional certification exam. Choose to follow an in-depth guide, or review select exam topics depending on the kind of preparation support you need. Terraform
- Terraform
On this page:

- What is Terraform?
[What is Terraform?](/terraform#what-is-terraform)
- Get Started
[Get Started](/terraform#get-started)
- Sandbox
[Sandbox](/terraform#sandbox)
- Best Practices
[Best Practices](/terraform#best-practices)
- Featured Documentation
[Featured Documentation](/terraform#featured-documentation)
- Popular Use Cases
[Popular Use Cases](/terraform#popular-use-cases)
- Get Certified
[Get Certified](/terraform#get-certified)
- Certifications
[Certifications](/certifications)
- System Status
[System Status](https://status.hashicorp.com)
- Cookie Manager
- Terms of Use
[Terms of Use](https://www.hashicorp.com/terms-of-service)
- Security
[Security](https://www.hashicorp.com/trust/security)
- Privacy
[Privacy](https://www.hashicorp.com/privacy)
- Trademark Policy
[Trademark Policy](https://www.hashicorp.com/trademark-policy)
- Trade Controls
[Trade Controls](https://www.hashicorp.com/trade-controls)
- Accessibility
[Accessibility](https://www.hashicorp.com/trust/accessibility)
- Give Feedback(opens in new tab)
[Give Feedback](https://forms.gle/fnHLuNahLEhjuKvE6)
- stdin is not a tty

---

## DOCUMENT: Terraform overview | Terraform | HashiCorp Developer
**Source:** https://developer.hashicorp.com/terraform/docs
**Ingested At:** 2026-05-23T11:14:56.512Z

### Introduction
[HashiConf 2025 Don't miss the live stream of HashiConf Day 2 happening now View live stream](https://www.hashicorp.com/conferences/hashiconf#livestream)
[All HCP Products](/hcp)
- Infrastructure Lifecycle ManagementTerraformManage infrastructure as codePackerBuild machine imagesNomadOrchestrate workloadsWaypointStandardize application patternsVagrantBuild developer environments
- TerraformManage infrastructure as code
[TerraformManage infrastructure as code](/terraform)
- PackerBuild machine images
[PackerBuild machine images](/packer)
- NomadOrchestrate workloads
[NomadOrchestrate workloads](/nomad)
- WaypointStandardize application patterns
[WaypointStandardize application patterns](/waypoint)
- VagrantBuild developer environments
[VagrantBuild developer environments](/vagrant)
- Security Lifecycle ManagementVaultCentrally manage secretsBoundarySecure remote accessVault RadarScan for embedded secretsConsulSecure network services
- VaultCentrally manage secrets
[VaultCentrally manage secrets](/vault)
- BoundarySecure remote access
[BoundarySecure remote access](/boundary)
- Vault RadarScan for embedded secrets
[Vault RadarScan for embedded secrets](/hcp/docs/vault-radar)
- ConsulSecure network services
[ConsulSecure network services](/consul)
- CertificationsGet HashiCorp certified
[CertificationsGet HashiCorp certified](/certifications)
- TutorialsLearn HashiCorp products
[TutorialsLearn HashiCorp products](/tutorials)
- Validated PatternsField-tested patterns for using HashiCorp products
[Validated PatternsField-tested patterns for using HashiCorp products](/validated-patterns)
- Well-Architected FrameworkAdopt HashiCorp best practices
[Well-Architected FrameworkAdopt HashiCorp best practices](/well-architected-framework)
[Terraform](/terraform)
- Install
[Install](/terraform/install)
- Tutorials
[Tutorials](/terraform/tutorials)
- DocumentationDocumentationIntro to TerraformConfiguration LanguageTerraform CLIHCP TerraformTerraform EnterpriseTerraform MCP ServerBETATerraform MigrateProvider UsePlugin DevelopmentRegistry PublishingIntegration Program
- Documentation
[Documentation](/terraform/docs)
- Intro to Terraform
[Intro to Terraform](/terraform/intro)
- Configuration Language
[Configuration Language](/terraform/language)
- Terraform CLI
[Terraform CLI](/terraform/cli)
- HCP Terraform
[HCP Terraform](/terraform/cloud-docs)
- Terraform Enterprise
[Terraform Enterprise](/terraform/enterprise)
- Terraform MCP ServerBETA
[Terraform MCP ServerBETA](/terraform/mcp-server)
- Terraform Migrate
[Terraform Migrate](/terraform/migrate)
- Provider Use
[Provider Use](/terraform/language/providers)
- Plugin Development
[Plugin Development](/terraform/plugin)
- Registry Publishing
[Registry Publishing](/terraform/registry)
- Integration Program
[Integration Program](/terraform/docs/partnerships)
- Sandbox
- Registry(opens in new tab)
[Registry](https://registry.terraform.io/)
- Try Cloud(opens in new tab)
[Try Cloud](https://app.terraform.io/public/signup/account)
- Sign in
- Sign up
[Sign up](/sign-up)
- Theme
[Terraform Home](/terraform)

### Documentation
- Documentation
[Documentation](/terraform/docs)
- Intro to Terraform
[Intro to Terraform](/terraform/intro)
- Configuration Language
[Configuration Language](/terraform/language)
- Terraform CLI
[Terraform CLI](/terraform/cli)
- HCP Terraform
[HCP Terraform](/terraform/cloud-docs)
- Terraform Enterprise
[Terraform Enterprise](/terraform/enterprise)
- CDK for Terraform
[CDK for Terraform](/terraform/cdktf)
- Provider Use
[Provider Use](/terraform/language/providers)
- Plugin Development
[Plugin Development](/terraform/plugin)
- Registry Publishing
[Registry Publishing](/terraform/registry)
- Integration Program
[Integration Program](/terraform/docs/partnerships)
- Terraform Tools
[Terraform Tools](/terraform/docs/tools)
- Glossary
[Glossary](/terraform/docs/glossary)
- Resources

### Resources
- Tutorial Library
[Tutorial Library](/tutorials/library?product=terraform)
- Certifications
[Certifications](/certifications/infrastructure-automation)
- Sandbox
[Sandbox](/terraform/sandbox)
- Community Forum(opens in new tab)
[Community Forum](https://discuss.hashicorp.com/c/terraform-core/27)
- Support(opens in new tab)
[Support](https://www.ibm.com/mysupport)
- GitHub(opens in new tab)
[GitHub](https://github.com/hashicorp/terraform)
- Terraform Registry(opens in new tab)
[Terraform Registry](https://registry.terraform.io/)
- Developer
[Developer](/)
- Terraform
[Terraform](/terraform)
- Documentation

### Terraform Documentation
Terraform is an infrastructure as code tool that lets you build, change, and version infrastructure safely and efficiently. This includes low-level components like compute instances, storage, and networking, as well as high-level components like DNS entries and SaaS features.

### Introduction
- What is Terraform?How Terraform solves infrastructure challenges.
- Use CasesPopular use cases and related documentation you can use to create Terraform configurations and workflows.
- Terraform vs. AlternativesLearn how Terraform compares to other tools and services.
- Phases of Terraform adoptionDesign your Terraform workflows for scale.

### Manage Infrastructure
- Configuration LanguageDescribe infrastructure on various providers with Terraform's configuration language.
- Terraform CLIUse the Terraform CLI to manage configuration, plugins, infrastructure, and state.

### Collaborate
- HCP TerraformHCP Terraform helps teams use Terraform together, with version control, state sharing, governance, and more.
- Terraform EnterpriseTerraform Enterprise is a self-hosted instance of HCP Terraform, which is ideal for organizations that have strict security and compliance requirements.

### Develop and Share
- Plugin DevelopmentCreate a provider to allow Terraform to interact with a service.
- ModulesCreate reusable configurations with modules.
- Registry PublishingPublish a provider or module to the Terraform Registry to make it publicly available.
On this page:

- Terraform Documentation
[Terraform Documentation](/terraform/docs#terraform-documentation)
- Introduction
[Introduction](/terraform/docs#introduction)
- Manage Infrastructure
[Manage Infrastructure](/terraform/docs#manage-infrastructure)
- Collaborate
[Collaborate](/terraform/docs#collaborate)
- Develop and Share
[Develop and Share](/terraform/docs#develop-and-share)
- Certifications
[Certifications](/certifications)
- System Status
[System Status](https://status.hashicorp.com)
- Cookie Manager
- Terms of Use
[Terms of Use](https://www.hashicorp.com/terms-of-service)
- Security
[Security](https://www.hashicorp.com/trust/security)
- Privacy
[Privacy](https://www.hashicorp.com/privacy)
- Trademark Policy
[Trademark Policy](https://www.hashicorp.com/trademark-policy)
- Trade Controls
[Trade Controls](https://www.hashicorp.com/trade-controls)
- Accessibility
[Accessibility](https://www.hashicorp.com/trust/accessibility)
- Give Feedback(opens in new tab)
[Give Feedback](https://forms.gle/fnHLuNahLEhjuKvE6)
- stdin is not a tty

---

## DOCUMENT: GitHub - hashicorp/terraform: Terraform enables you to safely and predictably create, change, and improve infrastructure. It is a source-available tool that codifies APIs into declarative configuration files that can be shared amongst team members, treated as code, edited, reviewed, and versioned. · GitHub
**Source:** https://github.com/hashicorp/terraform
**Ingested At:** 2026-05-23T11:14:58.238Z

### Introduction
[Skip to content](#start-of-content)

### Navigation Menu
[Sign in](/login?return_to=https%3A%2F%2Fgithub.com%2Fhashicorp%2Fterraform)
- PlatformAI CODE CREATIONGitHub CopilotWrite better code with AIGitHub SparkBuild and deploy intelligent appsGitHub ModelsManage and compare promptsMCP RegistryNewIntegrate external toolsDEVELOPER WORKFLOWSActionsAutomate any workflowCodespacesInstant dev environmentsIssuesPlan and track workCode ReviewManage code changesAPPLICATION SECURITYGitHub Advanced SecurityFind and fix vulnerabilitiesCode securitySecure your code as you buildSecret protectionStop leaks before they startEXPLOREWhy GitHubDocumentationBlogChangelogMarketplaceView all features
- AI CODE CREATIONGitHub CopilotWrite better code with AIGitHub SparkBuild and deploy intelligent appsGitHub ModelsManage and compare promptsMCP RegistryNewIntegrate external tools
- GitHub CopilotWrite better code with AI
[GitHub CopilotWrite better code with AI](https://github.com/features/copilot)
- GitHub SparkBuild and deploy intelligent apps
[GitHub SparkBuild and deploy intelligent apps](https://github.com/features/spark)
- GitHub ModelsManage and compare prompts
[GitHub ModelsManage and compare prompts](https://github.com/features/models)
- MCP RegistryNewIntegrate external tools
[MCP RegistryNewIntegrate external tools](https://github.com/mcp)
- DEVELOPER WORKFLOWSActionsAutomate any workflowCodespacesInstant dev environmentsIssuesPlan and track workCode ReviewManage code changes
- ActionsAutomate any workflow
[ActionsAutomate any workflow](https://github.com/features/actions)
- CodespacesInstant dev environments
[CodespacesInstant dev environments](https://github.com/features/codespaces)
- IssuesPlan and track work
[IssuesPlan and track work](https://github.com/features/issues)
- Code ReviewManage code changes
[Code ReviewManage code changes](https://github.com/features/code-review)
- APPLICATION SECURITYGitHub Advanced SecurityFind and fix vulnerabilitiesCode securitySecure your code as you buildSecret protectionStop leaks before they start
- GitHub Advanced SecurityFind and fix vulnerabilities
[GitHub Advanced SecurityFind and fix vulnerabilities](https://github.com/security/advanced-security)
- Code securitySecure your code as you build
[Code securitySecure your code as you build](https://github.com/security/advanced-security/code-security)
- Secret protectionStop leaks before they start
[Secret protectionStop leaks before they start](https://github.com/security/advanced-security/secret-protection)
- EXPLOREWhy GitHubDocumentationBlogChangelogMarketplace
- Why GitHub
[Why GitHub](https://github.com/why-github)
- Documentation
[Documentation](https://docs.github.com)
- Blog
[Blog](https://github.blog)
- Changelog
[Changelog](https://github.blog/changelog)
- Marketplace
[Marketplace](https://github.com/marketplace)
[View all features](https://github.com/features)
- SolutionsBY COMPANY SIZEEnterprisesSmall and medium teamsStartupsNonprofitsBY USE CASEApp ModernizationDevSecOpsDevOpsCI/CDView all use casesBY INDUSTRYHealthcareFinancial servicesManufacturingGovernmentView all industriesView all solutions
- BY COMPANY SIZEEnterprisesSmall and medium teamsStartupsNonprofits
- Enterprises
[Enterprises](https://github.com/enterprise)
- Small and medium teams
[Small and medium teams](https://github.com/team)
- Startups
[Startups](https://github.com/enterprise/startups)
- Nonprofits
[Nonprofits](https://github.com/solutions/industry/nonprofits)
- BY USE CASEApp ModernizationDevSecOpsDevOpsCI/CDView all use cases
- App Modernization
[App Modernization](https://github.com/solutions/use-case/app-modernization)
- DevSecOps
[DevSecOps](https://github.com/solutions/use-case/devsecops)
- DevOps
[DevOps](https://github.com/solutions/use-case/devops)

### - CI/CD
[CI/CD](https://github.com/solutions/use-case/ci-cd)
- View all use cases
[View all use cases](https://github.com/solutions/use-case)
- BY INDUSTRYHealthcareFinancial servicesManufacturingGovernmentView all industries
- Healthcare
[Healthcare](https://github.com/solutions/industry/healthcare)
- Financial services
[Financial services](https://github.com/solutions/industry/financial-services)
- Manufacturing
[Manufacturing](https://github.com/solutions/industry/manufacturing)
- Government
[Government](https://github.com/solutions/industry/government)
- View all industries
[View all industries](https://github.com/solutions/industry)
[View all solutions](https://github.com/solutions)
- ResourcesEXPLORE BY TOPICAISoftware DevelopmentDevOpsSecurityView all topicsEXPLORE BY TYPECustomer storiesEvents & webinarsEbooks & reportsBusiness insightsGitHub SkillsSUPPORT & SERVICESDocumentationCustomer supportCommunity forumTrust centerPartnersView all resources
- EXPLORE BY TOPICAISoftware DevelopmentDevOpsSecurityView all topics

### - AI
[AI](https://github.com/resources/articles?topic=ai)
- Software Development
[Software Development](https://github.com/resources/articles?topic=software-development)
- DevOps
[DevOps](https://github.com/resources/articles?topic=devops)
- Security
[Security](https://github.com/resources/articles?topic=security)
- View all topics
[View all topics](https://github.com/resources/articles)
- EXPLORE BY TYPECustomer storiesEvents & webinarsEbooks & reportsBusiness insightsGitHub Skills
- Customer stories
[Customer stories](https://github.com/customer-stories)
- Events & webinars
[Events & webinars](https://github.com/resources/events)
- Ebooks & reports
[Ebooks & reports](https://github.com/resources/whitepapers)
- Business insights
[Business insights](https://github.com/solutions/executive-insights)
- GitHub Skills
[GitHub Skills](https://skills.github.com)
- SUPPORT & SERVICESDocumentationCustomer supportCommunity forumTrust centerPartners
- Documentation
[Documentation](https://docs.github.com)
- Customer support
[Customer support](https://support.github.com)
- Community forum
[Community forum](https://github.com/orgs/community/discussions)
- Trust center
[Trust center](https://github.com/trust-center)
- Partners
[Partners](https://github.com/partners)
[View all resources](https://github.com/resources)
- Open SourceCOMMUNITYGitHub SponsorsFund open source developersPROGRAMSSecurity LabMaintainer CommunityAcceleratorGitHub StarsArchive ProgramREPOSITORIESTopicsTrendingCollections
- COMMUNITYGitHub SponsorsFund open source developers
- GitHub SponsorsFund open source developers
[GitHub SponsorsFund open source developers](https://github.com/sponsors)
- PROGRAMSSecurity LabMaintainer CommunityAcceleratorGitHub StarsArchive Program
- Security Lab
[Security Lab](https://securitylab.github.com)
- Maintainer Community
[Maintainer Community](https://maintainers.github.com)
- Accelerator
[Accelerator](https://github.com/accelerator)
- GitHub Stars
[GitHub Stars](https://stars.github.com)
- Archive Program
[Archive Program](https://archiveprogram.github.com)
- REPOSITORIESTopicsTrendingCollections
- Topics
[Topics](https://github.com/topics)
- Trending
[Trending](https://github.com/trending)
- Collections
[Collections](https://github.com/collections)
- EnterpriseENTERPRISE SOLUTIONSEnterprise platformAI-powered developer platformAVAILABLE ADD-ONSGitHub Advanced SecurityEnterprise-grade security featuresCopilot for BusinessEnterprise-grade AI featuresPremium SupportEnterprise-grade 24/7 support
- ENTERPRISE SOLUTIONSEnterprise platformAI-powered developer platform
- Enterprise platformAI-powered developer platform
[Enterprise platformAI-powered developer platform](https://github.com/enterprise)
- AVAILABLE ADD-ONSGitHub Advanced SecurityEnterprise-grade security featuresCopilot for BusinessEnterprise-grade AI featuresPremium SupportEnterprise-grade 24/7 support
- GitHub Advanced SecurityEnterprise-grade security features
[GitHub Advanced SecurityEnterprise-grade security features](https://github.com/security/advanced-security)
- Copilot for BusinessEnterprise-grade AI features
[Copilot for BusinessEnterprise-grade AI features](https://github.com/features/copilot/copilot-business)
- Premium SupportEnterprise-grade 24/7 support
[Premium SupportEnterprise-grade 24/7 support](https://github.com/premium-support)
- Pricing
[Pricing](https://github.com/pricing)

### Search code, repositories, users, issues, pull requests...
[Search syntax tips](https://docs.github.com/search-github/github-code-search/understanding-github-code-search-syntax)

### Provide feedback
We read every piece of feedback, and take your input very seriously.

### Saved searches


### Use saved searches to filter your results more quickly
To see all available qualifiers, see our documentation.

[documentation](https://docs.github.com/search-github/github-code-search/understanding-github-code-search-syntax)
[Sign in](/login?return_to=https%3A%2F%2Fgithub.com%2Fhashicorp%2Fterraform)
[Sign up](/signup?ref_cta=Sign+up&ref_loc=header+logged+out&ref_page=%2F%3Cuser-name%3E%2F%3Crepo-name%3E&source=header-repo&source_repo=hashicorp%2Fterraform)
[hashicorp](/hashicorp)
[terraform](/hashicorp/terraform)
- Notifications You must be signed in to change notification settings
[Notifications](/login?return_to=%2Fhashicorp%2Fterraform)
- Fork 10.3k
[Fork 10.3k](/login?return_to=%2Fhashicorp%2Fterraform)
- Star 48.4k
[Star 48.4k](/login?return_to=%2Fhashicorp%2Fterraform)
- Code
[Code](/hashicorp/terraform)
- Issues 1.8k
[Issues 1.8k](/hashicorp/terraform/issues)
- Pull requests 147
[Pull requests 147](/hashicorp/terraform/pulls)
- Actions
[Actions](/hashicorp/terraform/actions)
- Security and quality 1
[Security and quality 1](/hashicorp/terraform/security)
- Insights
[Insights](/hashicorp/terraform/pulse)
- Code
[Code](/hashicorp/terraform)
- Issues
[Issues](/hashicorp/terraform/issues)
- Pull requests
[Pull requests](/hashicorp/terraform/pulls)
- Actions
[Actions](/hashicorp/terraform/actions)
- Security and quality
[Security and quality](/hashicorp/terraform/security)
- Insights
[Insights](/hashicorp/terraform/pulse)

### hashicorp/terraform
[Branches](/hashicorp/terraform/branches)
[Tags](/hashicorp/terraform/tags)

### Folders and files


### Latest commit


### History
[35,438 Commits](/hashicorp/terraform/commits/main/)
[.changes](/hashicorp/terraform/tree/main/.changes)
[.changes](/hashicorp/terraform/tree/main/.changes)
[.github](/hashicorp/terraform/tree/main/.github)
[.github](/hashicorp/terraform/tree/main/.github)
[.release](/hashicorp/terraform/tree/main/.release)
[.release](/hashicorp/terraform/tree/main/.release)
[docs](/hashicorp/terraform/tree/main/docs)
[docs](/hashicorp/terraform/tree/main/docs)
[internal](/hashicorp/terraform/tree/main/internal)
[internal](/hashicorp/terraform/tree/main/internal)
[scripts](/hashicorp/terraform/tree/main/scripts)
[scripts](/hashicorp/terraform/tree/main/scripts)
[testing/equivalence-tests](/hashicorp/terraform/tree/main/testing/equivalence-tests)
[testing/equivalence-tests](/hashicorp/terraform/tree/main/testing/equivalence-tests)
[tools](/hashicorp/terraform/tree/main/tools)
[tools](/hashicorp/terraform/tree/main/tools)
[version](/hashicorp/terraform/tree/main/version)
[version](/hashicorp/terraform/tree/main/version)
[website](/hashicorp/terraform/tree/main/website)
[website](/hashicorp/terraform/tree/main/website)
[.changie.yaml](/hashicorp/terraform/blob/main/.changie.yaml)
[.changie.yaml](/hashicorp/terraform/blob/main/.changie.yaml)
[.copywrite.hcl](/hashicorp/terraform/blob/main/.copywrite.hcl)
[.copywrite.hcl](/hashicorp/terraform/blob/main/.copywrite.hcl)
[.git-blame-ignore-revs](/hashicorp/terraform/blob/main/.git-blame-ignore-revs)
[.git-blame-ignore-revs](/hashicorp/terraform/blob/main/.git-blame-ignore-revs)
[.gitignore](/hashicorp/terraform/blob/main/.gitignore)
[.gitignore](/hashicorp/terraform/blob/main/.gitignore)
[.go-version](/hashicorp/terraform/blob/main/.go-version)
[.go-version](/hashicorp/terraform/blob/main/.go-version)
[.tfdev](/hashicorp/terraform/blob/main/.tfdev)
[.tfdev](/hashicorp/terraform/blob/main/.tfdev)
[BUGPROCESS.md](/hashicorp/terraform/blob/main/BUGPROCESS.md)
[BUGPROCESS.md](/hashicorp/terraform/blob/main/BUGPROCESS.md)
[BUILDING.md](/hashicorp/terraform/blob/main/BUILDING.md)
[BUILDING.md](/hashicorp/terraform/blob/main/BUILDING.md)
[CHANGELOG.md](/hashicorp/terraform/blob/main/CHANGELOG.md)
[CHANGELOG.md](/hashicorp/terraform/blob/main/CHANGELOG.md)
[CODEOWNERS](/hashicorp/terraform/blob/main/CODEOWNERS)
[CODEOWNERS](/hashicorp/terraform/blob/main/CODEOWNERS)
[Dockerfile](/hashicorp/terraform/blob/main/Dockerfile)
[Dockerfile](/hashicorp/terraform/blob/main/Dockerfile)
[LICENSE](/hashicorp/terraform/blob/main/LICENSE)
[LICENSE](/hashicorp/terraform/blob/main/LICENSE)
[Makefile](/hashicorp/terraform/blob/main/Makefile)
[Makefile](/hashicorp/terraform/blob/main/Makefile)
[README.md](/hashicorp/terraform/blob/main/README.md)
[README.md](/hashicorp/terraform/blob/main/README.md)
[build.Dockerfile](/hashicorp/terraform/blob/main/build.Dockerfile)
[build.Dockerfile](/hashicorp/terraform/blob/main/build.Dockerfile)
[catalog-info.yaml](/hashicorp/terraform/blob/main/catalog-info.yaml)
[catalog-info.yaml](/hashicorp/terraform/blob/main/catalog-info.yaml)
[checkpoint.go](/hashicorp/terraform/blob/main/checkpoint.go)
[checkpoint.go](/hashicorp/terraform/blob/main/checkpoint.go)
[commands.go](/hashicorp/terraform/blob/main/commands.go)
[commands.go](/hashicorp/terraform/blob/main/commands.go)
[experiments.go](/hashicorp/terraform/blob/main/experiments.go)
[experiments.go](/hashicorp/terraform/blob/main/experiments.go)
[go.mod](/hashicorp/terraform/blob/main/go.mod)
[go.mod](/hashicorp/terraform/blob/main/go.mod)
[go.sum](/hashicorp/terraform/blob/main/go.sum)
[go.sum](/hashicorp/terraform/blob/main/go.sum)
[help.go](/hashicorp/terraform/blob/main/help.go)
[help.go](/hashicorp/terraform/blob/main/help.go)
[main.go](/hashicorp/terraform/blob/main/main.go)
[main.go](/hashicorp/terraform/blob/main/main.go)
[main_test.go](/hashicorp/terraform/blob/main/main_test.go)
[main_test.go](/hashicorp/terraform/blob/main/main_test.go)
[provider_source.go](/hashicorp/terraform/blob/main/provider_source.go)
[provider_source.go](/hashicorp/terraform/blob/main/provider_source.go)
[signal_unix.go](/hashicorp/terraform/blob/main/signal_unix.go)
[signal_unix.go](/hashicorp/terraform/blob/main/signal_unix.go)
[signal_windows.go](/hashicorp/terraform/blob/main/signal_windows.go)
[signal_windows.go](/hashicorp/terraform/blob/main/signal_windows.go)
[staticcheck.conf](/hashicorp/terraform/blob/main/staticcheck.conf)
[staticcheck.conf](/hashicorp/terraform/blob/main/staticcheck.conf)
[telemetry.go](/hashicorp/terraform/blob/main/telemetry.go)
[telemetry.go](/hashicorp/terraform/blob/main/telemetry.go)
[version.go](/hashicorp/terraform/blob/main/version.go)
[version.go](/hashicorp/terraform/blob/main/version.go)
[working_dir.go](/hashicorp/terraform/blob/main/working_dir.go)
[working_dir.go](/hashicorp/terraform/blob/main/working_dir.go)

### - README
[README](#)
- Code of conduct
[Code of conduct](#)
- Contributing
[Contributing](#)
- License
[License](#)
- Security
[Security](#)

### Terraform
- Website: https://developer.hashicorp.com/terraform
[https://developer.hashicorp.com/terraform](https://developer.hashicorp.com/terraform)
- Forums: HashiCorp Discuss
[HashiCorp Discuss](https://discuss.hashicorp.com/c/terraform-core)
- Documentation: https://developer.hashicorp.com/terraform/docs
[https://developer.hashicorp.com/terraform/docs](https://developer.hashicorp.com/terraform/docs)
- Tutorials: HashiCorp's Learn Platform
[HashiCorp's Learn Platform](https://developer.hashicorp.com/terraform/tutorials)
- Certification Exam: HashiCorp Certified: Terraform Associate
[HashiCorp Certified: Terraform Associate](https://www.hashicorp.com/certification/#hashicorp-certified-terraform-associate)
Terraform is a tool for building, changing, and versioning infrastructure safely and efficiently. Terraform can manage existing and popular service providers as well as custom in-house solutions.

The key features of Terraform are:

- Infrastructure as Code: Infrastructure is described using a high-level configuration syntax. This allows a blueprint of your datacenter to be versioned and treated as you would any other code. Additionally, infrastructure can be shared and re-used.
Infrastructure as Code: Infrastructure is described using a high-level configuration syntax. This allows a blueprint of your datacenter to be versioned and treated as you would any other code. Additionally, infrastructure can be shared and re-used.

- Execution Plans: Terraform has a "planning" step where it generates an execution plan. The execution plan shows what Terraform will do when you call apply. This lets you avoid any surprises when Terraform manipulates infrastructure.
Execution Plans: Terraform has a "planning" step where it generates an execution plan. The execution plan shows what Terraform will do when you call apply. This lets you avoid any surprises when Terraform manipulates infrastructure.

- Resource Graph: Terraform builds a graph of all your resources, and parallelizes the creation and modification of any non-dependent resources. Because of this, Terraform builds infrastructure as efficiently as possible, and operators get insight into dependencies in their infrastructure.
Resource Graph: Terraform builds a graph of all your resources, and parallelizes the creation and modification of any non-dependent resources. Because of this, Terraform builds infrastructure as efficiently as possible, and operators get insight into dependencies in their infrastructure.

- Change Automation: Complex changesets can be applied to your infrastructure with minimal human interaction. With the previously mentioned execution plan and resource graph, you know exactly what Terraform will change and in what order, avoiding many possible human errors.
Change Automation: Complex changesets can be applied to your infrastructure with minimal human interaction. With the previously mentioned execution plan and resource graph, you know exactly what Terraform will change and in what order, avoiding many possible human errors.

For more information, refer to the What is Terraform? page on the Terraform website.

[What is Terraform?](https://www.terraform.io/intro)

### Getting Started & Documentation
Documentation is available on the Terraform website:

[Terraform website](https://developer.hashicorp.com/terraform)
- Introduction
[Introduction](https://developer.hashicorp.com/terraform/intro)
- Documentation
[Documentation](https://developer.hashicorp.com/terraform/docs)
If you're new to Terraform and want to get started creating infrastructure, please check out our Getting Started guides on HashiCorp's learning platform. There are also additional guides to continue your learning.

[Getting Started guides](https://learn.hashicorp.com/terraform#getting-started)
[additional guides](https://learn.hashicorp.com/terraform#operations-and-development)
Show off your Terraform knowledge by passing a certification exam. Visit the certification page for information about exams and find study materials on HashiCorp's learning platform.

[certification page](https://www.hashicorp.com/certification/)
[study materials](https://learn.hashicorp.com/terraform/certification/terraform-associate)

### Developing Terraform
This repository contains only Terraform core, which includes the command line interface and the main graph engine. Providers are implemented as plugins, and Terraform can automatically download providers that are published on the Terraform Registry. HashiCorp develops some providers, and others are developed by other organizations. For more information, refer to Plugin development.

[the Terraform Registry](https://registry.terraform.io)
[Plugin development](https://developer.hashicorp.com/terraform/plugin)
- To learn more about compiling Terraform and contributing suggested changes, refer to the contributing guide.
To learn more about compiling Terraform and contributing suggested changes, refer to the contributing guide.

[the contributing guide](/hashicorp/terraform/blob/main/.github/CONTRIBUTING.md)
- To learn more about how we handle bug reports, refer to the bug triage guide.
To learn more about how we handle bug reports, refer to the bug triage guide.

[bug triage guide](/hashicorp/terraform/blob/main/BUGPROCESS.md)
- To learn how to contribute to the Terraform documentation, refer to the Web Unified Docs repository.
To learn how to contribute to the Terraform documentation, refer to the Web Unified Docs repository.

[Web Unified Docs repository](https://github.com/hashicorp/web-unified-docs)

### License
Business Source License 1.1

[Business Source License 1.1](https://github.com/hashicorp/terraform/blob/main/LICENSE)

### About
Terraform enables you to safely and predictably create, change, and improve infrastructure. It is a source-available tool that codifies APIs into declarative configuration files that can be shared amongst team members, treated as code, edited, reviewed, and versioned.

[developer.hashicorp.com/terraform](http://developer.hashicorp.com/terraform)

### Topics
[cloud](/topics/cloud)
[graph](/topics/graph)
[terraform](/topics/terraform)
[cloud-management](/topics/cloud-management)
[infrastructure-as-code](/topics/infrastructure-as-code)

### Resources
[Readme](#readme-ov-file)

### License
[View license](#License-1-ov-file)

### Code of conduct
[Code of conduct](#coc-ov-file)

### Contributing
[Contributing](#contributing-ov-file)

### Security policy
[Security policy](#security-ov-file)

### Uh oh!
There was an error while loading. Please reload this page.

[Activity](/hashicorp/terraform/activity)
[Custom properties](/hashicorp/terraform/custom-properties)

### Stars
[48.4k stars](/hashicorp/terraform/stargazers)

### Watchers
[1.1k watching](/hashicorp/terraform/watchers)

### Forks
[10.3k forks](/hashicorp/terraform/forks)
[Report repository](/contact/report-content?content_url=https%3A%2F%2Fgithub.com%2Fhashicorp%2Fterraform&report=hashicorp+%28user%29)

### Releases 418
[Releases 418](/hashicorp/terraform/releases)
[v1.15.4 Latest May 20, 2026](/hashicorp/terraform/releases/tag/v1.15.4)
[+ 417 releases](/hashicorp/terraform/releases)

### Uh oh!
There was an error while loading. Please reload this page.

### Contributors
[Contributors](/hashicorp/terraform/graphs/contributors)

### Uh oh!
There was an error while loading. Please reload this page.

### Languages
- Go 99.7%
[Go 99.7%](/hashicorp/terraform/search?l=go)
- Other 0.3%

### Footer


### Footer navigation
- Terms
[Terms](https://docs.github.com/site-policy/github-terms/github-terms-of-service)
- Privacy
[Privacy](https://docs.github.com/site-policy/privacy-policies/github-privacy-statement)
- Security
[Security](https://github.com/security)
- Status
[Status](https://www.githubstatus.com/)
- Community
[Community](https://github.community/)
- Docs
[Docs](https://docs.github.com/)
- Contact
[Contact](https://support.github.com?tags=dotcom-footer)
- Manage cookies
- Do not share my personal information

---
