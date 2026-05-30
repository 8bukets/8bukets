Push artifact metadata to the HCP Packer registry
6min
|
HCP
Packer

The HCP Packer registry aligns the workflows of artifact factories and artifact deployments, allowing operations and development teams to work together to create, manage, and consume artifacts from a centralized source. It helps downstream users retrieve the preferred versions of artifacts, manage dependencies in Packer build pipelines, and seamlessly track build artifacts across multiple regions and cloud providers.

In this tutorial, you will use Packer to build an AWS Amazon Machine Image (AMI) and push the image's metadata to the HCP Packer registry.

Prerequisites
This tutorial assumes that you are familiar with the standard Packer workflows. If you are new to Packer, complete the Get Started tutorials first.

To follow along with this tutorial, you will need:

Packer 1.10.1+ installed locally
An HCP account
An AWS account with credentials set as local environment variables. These credentials must have permissions to create, modify, and delete EC2 instances. Refer to the documentation to find the full list IAM permissions required to run the amazon-ebs builder.

Create HCP Packer registry
Go to the HashiCorp Cloud Platform portal. After logging in, you will find Packer under Services in the left navigation menu.

You must enable the HCP Packer registry before Packer can publish build metadata to it. Click the Create a registry button after clicking on the Packer link under Services in the left navigation. This only needs to be done once.

Create HCP service principal and set to environment variable
In your HCP project's dashboard, go to Access control (IAM) in the left navigation menu, then select the Service principals tab.

Create a service principal named packer with the Contributor role.

Once you create the service principal, HCP shows you a detailed overview page. Click Keys in the left navigation bar, then click Generate key to create a client ID and secret.

Copy and save the client ID and secret; you will not be able to retrieve the secret later. You will use these credentials in the next step.

Once you generate the keys for the service principal, set the client ID and secret as environment variables so that Packer can authenticate with HCP.

In your terminal, set an environment variable for the client ID.

$ export HCP_CLIENT_ID=

Then, set an environment variable for your client secret.

$ export HCP_CLIENT_SECRET=

Next, navigate to your HCP project settings page to get your project's ID.

Use this value to set an environment variable for your project's ID.

$ export HCP_PROJECT_ID=

Clone the example repository
In your terminal, clone the tutorial repository. It contains Packer template files to build an Ubuntu image and push its metadata to the HCP Packer registry. 16

$ git clone https://github.com/hashicorp-education/learn-hcp-packer-get-started

Navigate to the cloned repository.

$ cd learn-hcp-packer-get-started

Review Packer template
Open ubuntu-focal.pkr.hcl to review the template.

This Packer template uses the Packer Amazon plugin v1.0.2 or later.

There are two source blocks to build Ubuntu 20.04 AMIs, one for each of the us-east-2 and us-west-1 regions. This enables Packer to run your builds in parallel.

The hcp_packer_registry block lets you customize the metadata that Packer sends to HCP Packer registry. The block in this example defines the bucket's name (learn-packer-ubuntu), description, bucket labels and build labels.

ubuntu-focal.pkr.hcl

build {
  hcp_packer_registry {
    bucket_name = "learn-packer-ubuntu"
    description = "Description about the image being published."

    bucket_labels = {
      "owner"          = "platform-team"
      "os"             = "Ubuntu",
      "ubuntu-version" = "Focal 20.04",
    }

    build_labels = {
      "build-time"   = timestamp()
      "build-source" = basename(path.cwd)
    }
  }

  sources = [
    "source.amazon-ebs.basic-example-east",
    "source.amazon-ebs.basic-example-west"
  ]
}

Build the Packer artifact
Now that you have a template file configured for HCP Packer, you are ready to build the artifact and push its metadata to the registry.

First, initialize your Packer template.

$ packer init .

Now, format the Packer template.

$ packer fmt .

Finally, build your artifact. Packer displays color-coded output for both builds. You can tell which build source an output line is associated with by the line's color or prefix.

$ packer build ubuntu-focal.pkr.hcl
Tracking build on HCP Packer with fingerprint "01HMEY6Q765XFB19PBGY5FJKBK"
amazon-ebs.basic-example-east: output will be in this color.
amazon-ebs.basic-example-west: output will be in this color.

==> amazon-ebs.basic-example-east: Prevalidating any provided VPC information
==> amazon-ebs.basic-example-east: Prevalidating AMI Name: packer_AWS_1705603456_v1.0.0
==> amazon-ebs.basic-example-west: Prevalidating any provided VPC information
==> amazon-ebs.basic-example-west: Prevalidating AMI Name: packer_AWS_1705603457_v1.0.0
## ...
Build 'amazon-ebs.basic-example-west' finished after 4 minutes 29 seconds.

==> Wait completed after 4 minutes 29 seconds

==> Builds finished. The artifacts of successful builds are:
--> amazon-ebs.basic-example-east: AMIs were created:
us-east-2: ami-0fe50da2394a934f9

--> amazon-ebs.basic-example-east: Published metadata to HCP Packer registry packer/learn-packer-ubuntu/versions/01HMEY6QMW6H031QZ8EZPCNSMZ
--> amazon-ebs.basic-example-west: AMIs were created:
us-west-1: ami-02f909d884f6ddcc4

--> amazon-ebs.basic-example-west: Published metadata to HCP Packer registry packer/learn-packer-ubuntu/versions/01HMEY6QMW6H031QZ8EZPCNSMZ

Visit the AWS us-east-2 AMI Dashboard and us-west-1 AMI Dashboard to verify that Packer has built your artifacts.

Explore your bucket
Visit the HCP Packer dashboard to review the artifact metadata that Packer uploaded to the HCP Packer registry. The HCP Packer registry only stores the artifact metadata, not the artifact itself.

The main HCP Packer dashboard displays a list of buckets, the top-level category in the Packer registry. Each bucket maps to a Packer template. Notice the bucket's ID (learn-packer-ubuntu) corresponds to the bucket_name argument defined in your Packer template's build.hcp_packer_registry block.

Select the learn-packer-ubuntu bucket to find details about the artifact.

Here, you will find information about the bucket such as the description and labels. These are the values defined in your Packer template file's build.hcp_packer_registry block.

Explore artifact versions
Click on Versions in the left navigation menu.

Every time Packer builds a template, it creates an immutable record of the build called a version. A version may have multiple artifacts associated with it, depending on how many sources and destination regions your configuration defines. Packer gives each version a fingerprint using a randomly generated Unique Lexicographical Identifier (ULID) or the value set in the HCP_PACKER_BUILD_FINGERPRINT environment variable.

Click on the latest version.

Each version has at least one build that maps to the source configured in the Packer template. Each build has an immutable set of labels based on the Packer template (build_labels) at the time of build.

Click on us-east-2 to view the artifact ID and creation time associated with that build.

Next steps
In this tutorial, you used Packer to build AMIs and push the images' metadata to the HCP Packer registry. In the process, you learned more about the hcp_packer_registry block and HCP Packer buckets and versions.
