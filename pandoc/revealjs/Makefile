RESOURCE_DIR := resource
RESOURCES := $(shell find $(RESOURCE_DIR) -mindepth 1)
SLIDE_DIR := slide
PLUGIN_DIR := plugin


.PHONY: all
all: main.html slide.zip


main.html: main.md plugin/menu filter.py
	pandoc --mathjax -t revealjs -s $< | ./filter.py > $@


slide.zip: main.html $(RESOURCES) $(PLUGIN_DIR)/menu
	rm -rf $(SLIDE_DIR) $@
	mkdir $(SLIDE_DIR)
	cp -r $^ $(RESOURCE_DIR) $(PLUGIN_DIR) $(SLIDE_DIR)
	zip -r $@ $(SLIDE_DIR)


$(PLUGIN_DIR)/menu:
	git clone git@github.com:denehyg/reveal.js-menu $@


.PHONY: clean
clean:
	rm -rf main.html $(SLIDE_DIR) slide.zip plugin
