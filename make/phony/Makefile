QUERIES := view1.sql
VIEWS := view1.view


# %.sqlとパターンマッチで指定すると、最後にファイルは消去される。
# view1.sqlと直接していすると、消去されない。
# 一方で、view1.viewは、パターンマッチで指定していてもファイルは消去されない。
# たぶん、view1.viewの方は、allのprerequisiteとして直接に指定されている一方で、
# view1.sqlの方は、パターンマッチによってのみ生成されたファイル名だから・・かな。


all: view1.view
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
	rm -rf $(QUERIES) $(VIEWS) all
