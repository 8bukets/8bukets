output "kubeconfig_command" {
  description = "Command to generate the kubeconfig for the OKE cluster"
  value       = "oci ce cluster create-kubeconfig --cluster-id ${oci_containerengine_cluster.wp_cluster.id} --file $HOME/.kube/config --region ${var.region} --token-version 2.0.0  --kube-endpoint PUBLIC_ENDPOINT"
}

output "mysql_ip_address" {
  description = "Private IP address of the MySQL Database System"
  value       = oci_mysql_mysql_db_system.wp_mysql.ip_address
}

output "mysql_database_name" {
  description = "Default database name or connection info. By default MDS does not create a specific user DB, you will need to connect and create the 'wordpress' database."
  value       = "You will need to connect via an OKE pod or Bastion to create the 'wordpress' database."
}
