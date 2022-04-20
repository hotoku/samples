define func1
$(call func2,a b c)
endef


define func2
echo $(1) $(2) $(3)
endef


all:
	$(call func1)
