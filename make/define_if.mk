define f
ifeq ($(HOGE),hoge)
@echo HOGE is hoge
else
@echo HOGE is not hoge
endif
endef


all:
	$(call f)


# うまくいかない・・
# =>
# ifeq (hoge,hoge)
# /bin/sh: 1: Syntax error: word unexpected (expecting ")")
# make: *** [define_if.mk:11: all] Error 2
