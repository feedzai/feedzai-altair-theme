.PHONY: init

init:
	rm -rf .venv
	pip3 install pipenv==2022.1.8
	export PIPENV_VENV_IN_PROJECT=1 && \
	export VIRTUALENV_PIP=22.0.2 && \
	export VIRTUALENV_DOWNLOAD=1 && \
	pipenv install --python 3.7 --dev --deploy --ignore-pipfile --sequential
