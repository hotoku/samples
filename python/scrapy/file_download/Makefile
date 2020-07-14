PROJ_NAME=covid_pdf

.PHONY: run init
run:
	scrapy crawl CovidPdf


init: $(PROJ_NAME)/spiders/CovidPdf.py

$(PROJ_NAME)/spiders/CovidPdf.py: scrapy.cfg
	scrapy genspider CovidPdf www.city.akiruno.tokyo.jp

scrapy.cfg:
	scrapy startproject $(PROJ_NAME) .
	echo "DOWNLOAD_DELAY = 1" >> $(PROJ_NAME)/settings.py
	echo "FEED_EXPORT_ENCODING = 'utf-8'" >> $(PROJ_NAME)/settings.py
