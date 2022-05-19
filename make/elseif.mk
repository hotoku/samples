all:
ifeq ($(HOGE),hoge)
	@echo HOGE is hoge
else ifeq ($(HOGE),fuga)
	@echo HOGE is fuga
else
	@echo HOGE is $(HOGE)
endif
