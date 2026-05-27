.PHONY: docker-login docker-build docker-push

IMAGE_NAME ?= getanant/sor
TAG ?= latest

docker-login:
	@if [ -z "$(DOCKER_USERNAME)" ] || [ -z "$(DOCKER_PASSWORD)" ]; then \
		echo "Error: DOCKER_USERNAME and DOCKER_PASSWORD must be set."; \
		exit 1; \
	fi
	@echo "$(DOCKER_PASSWORD)" | docker login -u "$(DOCKER_USERNAME)" --password-stdin

docker-build:
	docker build -t $(IMAGE_NAME):$(TAG) .

docker-push: docker-login
	docker push $(IMAGE_NAME):$(TAG)
