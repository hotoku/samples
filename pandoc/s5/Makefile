.PHONY: all
all: s5 main.html slide.zip


main.html: main.md
	pandoc -t s5 -s $< -o $@


.PHONY: slide.zip
slide.zip: main.html s5
	$(eval DIST_DIR := slide)
	rm -rf $(DIST_DIR) $@
	mkdir $(DIST_DIR)
	cp -r $^ $(DIST_DIR)
	zip -r $@ $(DIST_DIR)


s5: s5_zip
	cp -r $</ui $@


s5_zip: s5-11.zip
	unzip -d $@ $<


.PHONY: clean
clean:
	rm -rf s5_zip s5 main.html slide.zip
