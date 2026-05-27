terraform {
  required_providers {
    tfe = {
      source  = "hashicorp/tfe"
      version = "~> 0.50.0"
    }
  }
}

provider "tfe" {
  token = var.tfe_token
}

resource "tfe_organization_run_task" "packer_validation" {
  organization = var.organization_name
  name         = "packer-validation"
  url          = var.endpoint_url
  hmac_key     = var.hmac_key
  description  = "Packer validation run task for HCP Terraform"
  category     = "task"
  enabled      = true
}
