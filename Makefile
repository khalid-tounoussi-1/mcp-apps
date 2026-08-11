.PHONY: help install validate build verify

help:
	@echo "make install   install python dependencies"
	@echo "make validate  check every apps/*.json against the schema"
	@echo "make build     regenerate apps.json and README.md"
	@echo "make verify    validate, then fail if generated files are stale"

install:
	python3 -m pip install -r requirements.txt

validate:
	python3 scripts/validate.py

build:
	python3 scripts/build.py

verify: validate
	python3 scripts/build.py --check
