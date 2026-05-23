# ANTIGRAVITY AI AGENTS KNOWLEDGE BASE

*Last Updated: 2026-05-23T05:24:24.852Z*

## DOCUMENT: Docker | Terraform | HashiCorp DeveloperInteractive
**Source:** https://developer.hashicorp.com/terraform/tutorials/docker-get-started
**Ingested At:** 2026-05-23T05:24:22.035Z

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
**Ingested At:** 2026-05-23T05:24:23.483Z

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
**Ingested At:** 2026-05-23T05:24:24.851Z

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

