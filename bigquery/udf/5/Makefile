.PHONY: run
run: copy
	cat udf.sql | bq query

copy: f.js
	gsutil cp f.js gs://us-central1-dev-004-5acd9ac2-bucket/f.js
	gsutil acl ch -u AllUsers:R gs://us-central1-dev-004-5acd9ac2-bucket/f.js
	touch $@
