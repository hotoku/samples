N := 1
M := 0

.PHONY: all

define POSITIVE
$(if $(shell if [ $1 -gt 0 ]; then echo 1; fi),positive)
endef

all:
	@echo $(call POSITIVE,$(N))
	@echo $(call POSITIVE,$(M))
