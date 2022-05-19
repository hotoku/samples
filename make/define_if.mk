define f
ifeq ($(HOGE),hoge)
@echo HOGE is hoge
else
@echo HOGE is not hoge
endif
endef


all:
	$(call, f)


# make -f if.mk # => HOGE is not hoge
# make -f if.mk HOGE=hoge # => Hoge is hoge
