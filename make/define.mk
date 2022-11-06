define f
echo a
echo b
echo $1
endef


all:
	$(call f,c)
