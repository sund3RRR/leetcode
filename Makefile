.PHONY: setup upgrade test

setup:
	python3 -m venv venv && ./venv/bin/python3 -m pip install -U pytest

upgrade:
	./venv/bin/python3 -m pip install --upgrade pip

test:
	./venv/bin/pytest .
