# macro & var
MAX_NUM := $(shell ls *.sql | sort -n | sed -e "s/.sql//" | tail -n1)
NUMS := $(shell seq 1 $(MAX_NUM))

define EXE_RULE
executed.$1: executed.$(shell expr $1 - 1)
endef


# rules
.PHONY: all 

all: executed.$(MAX_NUM)
	@echo $(MAX_NUM)

$(foreach i,$(NUMS),$(eval $(call EXE_RULE,$(i))))

executed.%: %.sql
	@echo $< && touch $@
