.PHONY: test clean install
test: dist/sample.js
	npm run-script test

dist/sample.js:
	npm run-script build

clean:
	rm -rf dist

install:
	npm i
