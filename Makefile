SHELL=bash

PROJECT_NAME=loadtest
ECR_REPO_URL=107164128218.dkr.ecr.eu-west-1.amazonaws.com/springboothelloworld5ef0240a-4qimqehrzasc

build-gradle:
	./gradlew build
.PHONY: build-gradle

build-docker: build-gradle
	docker build -t ${PROJECT_NAME}:latest .
.PHONY: build-docker

run: build-docker
	docker run -p 8080:8080 ${PROJECT_NAME}:latest
.PHONY: run

debug: build-docker
	docker run -ti --rm ${PROJECT_NAME}:latest /bin/ash
.PHONY: run

docker-push: build-docker
	docker tag ${PROJECT_NAME}:latest ${ECR_REPO_URL}:v24
	docker push ${ECR_REPO_URL}:v24
.PHONY: docker-push
