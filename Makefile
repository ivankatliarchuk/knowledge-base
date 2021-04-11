SHELL := /bin/bash
.ONESHELL:
.SHELLFLAGS := -eu -o pipefail -c
MAKEFLAGS += --warn-undefined-variables
MAKEFLAGS += --no-builtin-rules

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

requirements: ## Generate requirements.txt
	@pipenv run pip freeze > requirements.txt

run-on-container: ## Run on container
	@docker run --rm -it \
	-v ${PWD}:/tmp -w /tmp \
	lycheeverse/lychee \
    --verbose --no-progress --accept=200,403,429 \
    --exclude="^(javascript|chrome):.*" \
    --output out.md "docs/**/*.md" "README.md"
