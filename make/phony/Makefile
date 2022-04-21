TEMPLATES := view1.sql.jinja
QUERIES := view1.sql
VIEWS := view1.view


all: $(VIEWS)
	@echo "making all: $@ <- ($^)"
	@cat $^ > $@
	@echo "all done" >> $@


%.view: %.sql
	@echo "making view: $@"
	@cat $< > $@
	@echo "this is view ($@)" >> $@


%.sql:
	@echo "making query: $@ <- ($^)" > $@
	@echo "this is query" >> $@


.PHONY: clean
clean:
	rm -rf $(TEMPLATES) $(QUERIES) $(VIEWS) all
