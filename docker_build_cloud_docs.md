# Docker Build Cloud Setup

Before you can start using Docker Build Cloud, you must add the builder to your local environment.

## Prerequisites
To get started with Docker Build Cloud, you need to:

1. Download and install Docker Desktop version 4.26.0 or later.
2. Create a cloud builder on the Docker Build Cloud Dashboard.
3. When you create the builder, choose a name for it (for example, default). You will use this name as `BUILDER_NAME` in the CLI steps below.

## Use Docker Build Cloud without Docker Desktop
To use Docker Build Cloud without Docker Desktop, you must download and install a version of Buildx with support for Docker Build Cloud (the cloud driver). You can find compatible Buildx binaries on the releases page of this repository.

If you plan on building with Docker Build Cloud using the `docker compose build` command, you also need a version of Docker Compose that supports Docker Build Cloud. You can find compatible Docker Compose binaries on the releases page of this repository.

## Steps
You can add a cloud builder using the CLI, with the `docker buildx create` command, or using the Docker Desktop settings GUI.

### CLI
Sign in to your Docker account.
```bash
docker login
```

Add the cloud builder endpoint.
```bash
docker buildx create --driver cloud ORG/BUILDER_NAME
```

Replace `<ORG>` with the Docker Hub namespace of your Docker organization (or your username if you are using a personal account), and `<BUILDER_NAME>` with the name you chose when creating the builder in the dashboard.

This creates a local instance of the cloud builder named `cloud-ORG-BUILDER_NAME`.

**Note:** If your organization is acme and you named your builder default, use:
```bash
docker buildx create --driver cloud acme/default
```

The builder has native support for the linux/amd64 and linux/arm64 architectures. This gives you a high-performance build cluster for building multi-platform images natively.

## Firewall configuration
To use Docker Build Cloud behind a firewall, ensure that your firewall allows traffic to the following addresses:
- 3.211.38.21
- https://auth.docker.io
- https://build-cloud.docker.com
- https://hub.docker.com
