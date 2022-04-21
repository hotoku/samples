all: target.view
	@echo "making all: $@ <- ($^)"


%.view: %.sql
	@echo "making view: $@ <- ($^)"
	@cp $< $@
	@echo "this is view" >> $@


%.sql:
	@echo "making sql: $@ <- ($^)"
	@echo "this is sql" >> $@
