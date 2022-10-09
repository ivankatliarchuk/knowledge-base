SHELL := /bin/bash
.ONESHELL:
.SHELLFLAGS := -eu -o pipefail -c
MAKEFLAGS += --warn-undefined-variables
MAKEFLAGS += --no-builtin-rules

DOCKER_IMAGE := mkdocs

help:
	@printf "Usage: make [target] [VARIABLE=value]\nTargets:\n"
	@grep -E '^[a-zA-Z0-9_-]+:.*?## .*$$' $(MAKEFILE_LIST) | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'

# install: ## Install locally

shell: ## Python environment
	@pipenv shell
	@pipenv sync
	@pipenv install

hooks: ## Setup pre commit.
	@pre-commit install
	@pre-commit gc
	@pre-commit autoupdate

validate: ## Validate files with pre-commit hooks
	@pre-commit run --all-files

start: ## Start it
	@mkdocs serve
	# @open "http://127.0.0.1:8000"

docker-build: ## Build docker image
	@docker build -t $(DOCKER_IMAGE) .

docker-exec: ## Run docker locally
	@docker run --rm -it -p 8000:8000 -v ${PWD}:/docs $(DOCKER_IMAGE) /bin/bash

docker-run: ## Run docker locally
	@docker run --rm -it -p 8000:8000 -v ${PWD}:/docs $(DOCKER_IMAGE)

requirements: ## Generate requirements.txt
	@pipenv run pip freeze > requirements.txt

deps: ## Install dependencies
	@pip install -r requirements.txt

run-link-checker: ## Run on container
	@docker run --rm -it \
	-v ${PWD}:/tmp -w /tmp \
	lycheeverse/lychee \
	--verbose --no-progress --accept=200,403,429 \
	--exclude="^(javascript|chrome):.*" \
	--output out.md "docs/**/*.md" "README.md"
