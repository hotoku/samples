RESOURCE_DIR := resource
RESOURCES := $(shell find $(RESOURCE_DIR) -mindepth 1)
SLIDE_DIR := slide


.PHONY: all
all: main.html slide.zip


main.html: main.md $(RESOURCES)
	pandoc -t slidy -s $< -o $@


slide.zip: main.html $(RESOURCES)
	rm -rf $(SLIDE_DIR) $@
	mkdir $(SLIDE_DIR)
	cp -r $^ $(RESOURCE_DIR) $(SLIDE_DIR)
	zip -r $@ $(SLIDE_DIR)


.PHONY: clean
clean:
	rm -rf main.html $(SLIDE_DIR) slide.zip
