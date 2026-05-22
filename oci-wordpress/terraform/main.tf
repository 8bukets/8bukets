terraform {
  required_providers {
    oci = {
      source  = "oracle/oci"
      version = ">= 4.0.0"
    }
  }
}

provider "oci" {
  tenancy_ocid     = var.tenancy_ocid
  user_ocid        = var.user_ocid
  fingerprint      = var.fingerprint
  private_key_path = var.private_key_path
  region           = var.region
}

# VCN
resource "oci_core_vcn" "wordpress_vcn" {
  compartment_id = var.compartment_id
  cidr_block     = "10.0.0.0/16"
  display_name   = "wordpress-vcn"
  dns_label      = "wpvcn"
}

# Internet Gateway
resource "oci_core_internet_gateway" "igw" {
  compartment_id = var.compartment_id
  vcn_id         = oci_core_vcn.wordpress_vcn.id
  display_name   = "wordpress-igw"
  enabled        = true
}

# Default Route Table
resource "oci_core_default_route_table" "default_rt" {
  manage_default_resource_id = oci_core_vcn.wordpress_vcn.default_route_table_id

  route_rules {
    destination       = "0.0.0.0/0"
    destination_type  = "CIDR_BLOCK"
    network_entity_id = oci_core_internet_gateway.igw.id
  }
}

# Security List for OKE Nodes
resource "oci_core_security_list" "oke_sl" {
  compartment_id = var.compartment_id
  vcn_id         = oci_core_vcn.wordpress_vcn.id
  display_name   = "oke-security-list"

  # Egress to all
  egress_security_rules {
    destination = "0.0.0.0/0"
    protocol    = "all"
  }

  # Ingress for Kubernetes Control Plane (6443), LoadBalancer healthchecks/node ports
  ingress_security_rules {
    protocol = "6" # TCP
    source   = "0.0.0.0/0"
    tcp_options {
      max = 6443
      min = 6443
    }
  }

  # Ingress for HTTP to LoadBalancer NodePort range and HTTP 80
  ingress_security_rules {
    protocol = "6" # TCP
    source   = "0.0.0.0/0"
    tcp_options {
      max = 80
      min = 80
    }
  }

  # Ingress for inter-node communication
  ingress_security_rules {
    protocol = "all"
    source   = "10.0.1.0/24"
  }
}

# Subnet for OKE Nodes
resource "oci_core_subnet" "oke_subnet" {
  compartment_id    = var.compartment_id
  vcn_id            = oci_core_vcn.wordpress_vcn.id
  cidr_block        = "10.0.1.0/24"
  display_name      = "oke-subnet"
  route_table_id    = oci_core_vcn.wordpress_vcn.default_route_table_id
  security_list_ids = [oci_core_security_list.oke_sl.id]
}

# Security List for MySQL
resource "oci_core_security_list" "mysql_sl" {
  compartment_id = var.compartment_id
  vcn_id         = oci_core_vcn.wordpress_vcn.id
  display_name   = "mysql-security-list"

  egress_security_rules {
    destination = "0.0.0.0/0"
    protocol    = "all"
  }

  # Allow ingress on 3306 from OKE subnet
  ingress_security_rules {
    protocol = "6" # TCP
    source   = "10.0.1.0/24"
    tcp_options {
      max = 3306
      min = 3306
    }
  }
}

# Subnet for MySQL
resource "oci_core_subnet" "mysql_subnet" {
  compartment_id    = var.compartment_id
  vcn_id            = oci_core_vcn.wordpress_vcn.id
  cidr_block        = "10.0.2.0/24"
  display_name      = "mysql-subnet"
  prohibit_public_ip_on_vnic = true
  route_table_id    = oci_core_vcn.wordpress_vcn.default_route_table_id
  security_list_ids = [oci_core_security_list.mysql_sl.id]
}

# OKE Cluster
resource "oci_containerengine_cluster" "wp_cluster" {
  compartment_id     = var.compartment_id
  kubernetes_version = "v1.28.2" # Adjust as needed for current supported versions
  name               = "wordpress-cluster"
  vcn_id             = oci_core_vcn.wordpress_vcn.id

  endpoint_config {
    is_public_ip_enabled = true
    subnet_id            = oci_core_subnet.oke_subnet.id
  }

  options {
    add_ons {
      is_kubernetes_dashboard_enabled = false
      is_tiller_enabled               = false
    }
    kubernetes_network_config {
      pods_cidr     = "10.244.0.0/16"
      services_cidr = "10.96.0.0/16"
    }
  }
}

# OKE Node Pool
resource "oci_containerengine_node_pool" "wp_node_pool" {
  cluster_id         = oci_containerengine_cluster.wp_cluster.id
  compartment_id     = var.compartment_id
  kubernetes_version = "v1.28.2"
  name               = "wp-node-pool"
  node_shape         = "VM.Standard.E4.Flex"

  node_shape_config {
    memory_in_gbs = 16
    ocpus         = 2
  }

  node_source_details {
    image_id    = var.node_image_id # Needs to be defined in variables or looked up
    source_type = "IMAGE"
  }

  node_config_details {
    placement_configs {
      availability_domain = var.availability_domain
      subnet_id           = oci_core_subnet.oke_subnet.id
    }
    size = 2
  }
}

# MySQL Database Service (MDS)
resource "oci_mysql_mysql_db_system" "wp_mysql" {
  admin_password      = var.mysql_admin_password
  admin_username      = var.mysql_admin_username
  availability_domain = var.availability_domain
  compartment_id      = var.compartment_id
  shape_name          = "MySQL.VM.Standard.E4.1.8GB"
  subnet_id           = oci_core_subnet.mysql_subnet.id
  display_name        = "wordpress-mysql"

  data_storage_size_in_gb = 50

  # Ensure HeatWave is not strictly required if just regular MDS is needed,
  # but can be enabled if HeatWave cluster is added. For simple WP, standard MDS is fine.
}
