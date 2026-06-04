variable "tenancy_ocid" {
  description = "OCI Tenancy OCID"
  type        = string
}

variable "user_ocid" {
  description = "OCI User OCID"
  type        = string
}

variable "fingerprint" {
  description = "OCI API Key Fingerprint"
  type        = string
}

variable "private_key_path" {
  description = "Path to OCI API Private Key"
  type        = string
}

variable "region" {
  description = "OCI Region (e.g., us-ashburn-1)"
  type        = string
}

variable "compartment_id" {
  description = "Compartment OCID where resources will be created"
  type        = string
}

variable "availability_domain" {
  description = "The Availability Domain to deploy resources (e.g., uCwc:US-ASHBURN-AD-1)"
  type        = string
}

variable "node_image_id" {
  description = "OCID of the Oracle Linux image for OKE nodes"
  type        = string
}

variable "mysql_admin_username" {
  description = "Username for the MySQL Administrator"
  type        = string
  default     = "wpadmin"
}

variable "mysql_admin_password" {
  description = "Password for the MySQL Administrator"
  type        = string
  sensitive   = true
}
