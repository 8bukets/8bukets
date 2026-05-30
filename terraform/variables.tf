variable "organization_name" {
  description = "Name of the HCP Terraform Organization"
  type        = string
  default     = "626eb9aa-6f12-40a0-af3c-0b8fc325049e"
}

variable "endpoint_url" {
  description = "The endpoint URL for the run task"
  type        = string
  default     = "https://api.cloud.hashicorp.com/packer/2023-01-01/terraform-cloud/validation/f638d299-57d6-4ea4-96c5-d936811c468f"
}

variable "hmac_key" {
  description = "The HMAC key for the run task"
  type        = string
  sensitive   = true
}

variable "tfe_token" {
  description = "HCP Terraform API Token"
  type        = string
  sensitive   = true
}
