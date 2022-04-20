.PHONY: init format format_check lint type_check jupyter all

init:
	rm -rf .venv
	pip3 install pipenv==2022.1.8
	export PIPENV_VENV_IN_PROJECT=1 && \
	export VIRTUALENV_PIP=22.0.2 && \
	export VIRTUALENV_DOWNLOAD=1 && \
	pipenv install --python 3.7 --dev --deploy --ignore-pipfile --sequential

format:
	pipenv run isort .
	pipenv run black .

format_check:
	pipenv run isort --check .
	pipenv run black --check .

lint:
	pipenv run flake8 .

type_check:
	pipenv run mypy .

jupyter:
	pipenv run jupyter lab

all: type_check format lint
