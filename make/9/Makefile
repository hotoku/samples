MAX_NUM := 7


define EXE_RULE
executed.$1: executed.$(shell expr $1 - 1)
endef


.PHONY: all 

all: executed.$(MAX_NUM)
	@echo all

NUMS := $(shell seq 2 $(MAX_NUM))
$(foreach i,$(NUMS),$(eval $(call EXE_RULE,$(i))))

executed.%:
	@echo $<
