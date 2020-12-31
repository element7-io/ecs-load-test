SHELL=bash

PROJECT_NAME=loadtest

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
