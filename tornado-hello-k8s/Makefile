SHELL=/bin/bash

# if use another registry add  REGISTRY=registry.lisong.pub:5000 to ~/.bashrc
ifndef REGISTRY
    REGISTRY=registry.cn-hangzhou.aliyuncs.com
endif

REGISTRY_NAMESPACE=lisong
VERSION=v1.0
PROJECT_NAME=tornado-hello-k8s

IMAGE_TAG=$(VERSION).$(shell git rev-parse --short HEAD)
IMAGE=$(REGISTRY)/$(REGISTRY_NAMESPACE)/$(PROJECT_NAME)
VERSIONED_IMAGE=$(IMAGE):$(IMAGE_TAG)


# Push to registry. 推送到远程仓库
push:
	docker push $(VERSIONED_IMAGE)
	

pull:
	docker pull $(VERSIONED_IMAGE)
	
code:
	git reset --hard HEAD && git pull

build:
    cat $(VERSION) > version.txt
	docker build --no-cache -t $(VERSIONED_IMAGE) .

test:
	docker run --rm $(VERSIONED_IMAGE)


.PHONY: push pull build test start