.PHONY: noquote quote

noquote:
	bq load  --source_format=CSV --replace dtws-user-yasunori-horikoshi:temp.load 1.csv 1.json

quote:
	bq load  --source_format=CSV --replace --quote="" dtws-user-yasunori-horikoshi:temp.load 1.csv 1.json
