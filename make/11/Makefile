.PHONY: all a b c

all: a b c
	@echo atmarkt is $@
	@echo "<" is $<
	@echo "^" is $^
	@echo "first" is $(firstword $^)
	@echo "last" is $(lastword $^)
	@echo "n" is $(word 2,$^)

%:
	@echo target is $@
