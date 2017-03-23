.PHONY: generate test uninstall install

API_KEY=$(shell cat .env | grep google.api_key)

generate:
	python src/generate.py

test:
	pytest

uninstall:
	psql test -f uninstall.sql

install:
	psql test -c "set $(API_KEY)"
	psql test -f install_types.sql
	psql test -f install_py.sql
	psql test -f install_api.sql
