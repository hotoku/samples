PROJ_NAME=navitime
CLASS_NAME=Navitime
DOMAIN=https://www.navitime.co.jp


.PHONY: run init
run:
	scrapy crawl $(CLASS_NAME)


init: $(PROJ_NAME)/spiders/$(CLASS_NAME).py

$(PROJ_NAME)/spiders/$(CLASS_NAME).py: scrapy.cfg
	scrapy genspider $(CLASS_NAME) $(NAVITIME)

scrapy.cfg:
	scrapy startproject $(PROJ_NAME) .
	echo "DOWNLOAD_DELAY = 1" >> $(PROJ_NAME)/settings.py
	echo "FEED_EXPORT_ENCODING = 'utf-8'" >> $(PROJ_NAME)/settings.py
