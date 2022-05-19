all:
ifeq ($(HOGE),hoge)
	@echo HOGE is hoge
else
	@echo HOGE is not hoge
endif


# make -f if.mk => Hoge is not hoge
# make -f if.mk HOGE=hoge => Hoge is not hoge
