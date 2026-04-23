.PHONY: docker-build docker-push help

IMAGE_NAME ?= getanant/sor
TAG_NAME ?= tagname

help: ## Show this help
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-20s\033[0m %s\n", $$1, $$2}'

docker-build: ## Build the Docker image locally
	docker build -t $(IMAGE_NAME):$(TAG_NAME) .

docker-push: docker-build ## Build and push the Docker image to registry
	@if [ -z "$$DOCKER_USERNAME" ] || [ -z "$$DOCKER_PASSWORD" ]; then \
		echo "❌ Error: DOCKER_USERNAME and DOCKER_PASSWORD must be set to push."; \
		echo "Usage: DOCKER_USERNAME=myuser DOCKER_PASSWORD=mypass make docker-push"; \
		exit 1; \
	fi
	@echo "$$DOCKER_PASSWORD" | docker login -u "$$DOCKER_USERNAME" --password-stdin
	docker push $(IMAGE_NAME):$(TAG_NAME)
