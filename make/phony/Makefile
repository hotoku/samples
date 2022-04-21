QUERIES := view1.sql
VIEWS := view1.view


all: view1.view
	@echo "making all: $@ <- ($^)"
	@cat $^ > $@
	@echo "all done" >> $@


%.view: %.sql
	@echo "making view: $@"
	@cat $< > $@
	@echo "this is view ($@)" >> $@


# %.sqlとパターンマッチで指定すると、最後にファイルは消去される。
# view1.sqlと直接していすると、消去されない。
%.sql:
	@echo "making query: $@ <- ($^)" > $@
	@echo "this is query" >> $@


.PHONY: clean
clean:
	rm -rf $(QUERIES) $(VIEWS) all
