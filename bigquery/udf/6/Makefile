.PHONY: test clean install



SRC:=$(shell find src -type f -name "*.js")



test: dist/sample.js dist/func.sql
	npm run-script test
	cat dist/func.sql | bq query

dist/func.sql: sql/func.jinja.sql build/sample-var.js
	mkdir -p build 
	cp $< build
	jinja2 $(subst sql/,build/,$<) > $@

dist/sample.js build/sample-var.js: $(SRC)
	npm run-script build

clean:
	rm -rf dist build

install:
	npm i
