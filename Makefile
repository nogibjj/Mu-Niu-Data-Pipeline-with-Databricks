install:
	pip install --upgrade pip &&\
		pip install -r requirements.txt

format:
	black mylib/*.py

lint:
	ruff mylib/*.py

test:
	# test

deploy:
	# deploy goes here
		
all: install format lint test