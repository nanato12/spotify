.PHONY: init
init:
	test -f .env || cp .env.template .env
	pip install --upgrade pip
	pip install -r requirements.txt
	pip install -r requirements-dev.txt

.PHONY: lint
lint:
	black .
	flake8 .
	isort .
	mypy .

.PHONY: clear
clear:
	rm -rf venv

.PHONY: add-pkg
add-pkg:
	pip freeze | grep ${NAME} >> requirements.txt

.PHONY: run
run:
	python main.py
