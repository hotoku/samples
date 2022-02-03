.PHONY: all
all: s5 main.html


main.html: main.md
	pandoc -t s5 -s $< -o $@


s5: s5_zip
	ln -s $</ui $@


s5_zip: s5-11.zip
	unzip -d $@ $<


.PHONY: clean
clean:
	rm -rf s5_zip s5 main.html
