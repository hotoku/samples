news.jl:
	scrapy crawl news -o $@


.PHONY: shell
shell:
	scrapy shell https://news.yahoo.co.jp/pickup/6365123


.PHONY: spider-init
spider-init:
	scrapy genspider news news.yahoo.co.jp

