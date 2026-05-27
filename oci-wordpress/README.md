# Deploy WordPress on OCI with OKE and MySQL Database Service

This repository provides instructions and code for deploying a high-availability WordPress application on Oracle Cloud Infrastructure (OCI). The infrastructure uses OCI managed services, including Oracle Kubernetes Engine (OKE) for running the WordPress application and the MySQL Database Service (MDS) for external database storage.

## Architecture

*   **Virtual Cloud Network (VCN)**: A VCN is created with public subnets for the OKE cluster and private subnets for the MySQL database to ensure security.
*   **Oracle Kubernetes Engine (OKE)**: A managed Kubernetes service runs the WordPress pods.
*   **MySQL Database Service (MDS)**: A fully managed database service in OCI is used to store WordPress data. This separates the database layer from the application layer for better reliability and performance.
*   **Load Balancer**: An OCI Load Balancer is automatically provisioned via the Kubernetes `Service` to expose WordPress to the internet.
*   **Block Volume**: A Persistent Volume Claim (PVC) using OCI Block Storage ensures WordPress media uploads (`wp-content`) are not lost if a pod restarts.

## Prerequisites

Before starting, ensure you have the following installed and configured:

1.  [OCI CLI](https://docs.oracle.com/en-us/iaas/Content/API/SDKDocs/cliinstall.htm) configured with your tenant details.
2.  [Terraform](https://www.terraform.io/downloads.html) installed.
3.  [kubectl](https://kubernetes.io/docs/tasks/tools/) installed.

## Step 1: Provision Infrastructure with Terraform

1.  Navigate to the `terraform/` directory:
    ```bash
    cd terraform
    ```
2.  Create a `terraform.tfvars` file and provide the required variables (e.g., `tenancy_ocid`, `user_ocid`, `fingerprint`, `private_key_path`, `region`, `compartment_id`, `availability_domain`, `node_image_id`, `mysql_admin_password`).
3.  Initialize Terraform:
    ```bash
    terraform init
    ```
4.  Plan the infrastructure deployment:
    ```bash
    terraform plan
    ```
5.  Apply the configuration to create the resources:
    ```bash
    terraform apply
    ```
6.  Once completed, Terraform will output the command to configure `kubectl` and the private IP address of the MySQL database. Note these down.

## Step 2: Configure the Database

OCI MySQL Database Service provides the server, but you need to create the database for WordPress to use.

1.  Since the database is in a private subnet, you will need a bastion host, or you can temporarily run a MySQL client pod inside your OKE cluster to connect to the database.
2.  Connect to the MySQL instance using the IP address from the Terraform output and the admin credentials you specified.
3.  Run the following SQL commands:
    ```sql
    CREATE DATABASE wordpress;
    ```

## Step 3: Deploy WordPress on OKE

1.  Generate the kubeconfig using the command provided in the Terraform output.
    ```bash
    oci ce cluster create-kubeconfig ...
    ```
2.  Navigate to the `kubernetes/` directory:
    ```bash
    cd ../kubernetes
    ```
3.  Update the `mysql-secret.yaml` file with your actual MySQL password.
4.  Update the `wordpress-deployment.yaml` file by replacing `MYSQL_IP_ADDRESS` with the actual IP address of your MySQL instance from the Terraform output.
5.  Apply the Kubernetes manifests:
    ```bash
    kubectl apply -f mysql-secret.yaml
    kubectl apply -f wordpress-pvc.yaml
    kubectl apply -f wordpress-deployment.yaml
    kubectl apply -f wordpress-service.yaml
    ```
6.  Wait for the LoadBalancer to get an external IP:
    ```bash
    kubectl get services wordpress --watch
    ```

## Step 4: Access WordPress

Once the `EXTERNAL-IP` is populated for the `wordpress` service, open that IP address in your web browser. You will be greeted by the famous 5-minute WordPress installation screen.
