subdirs := a b

.PHONY: all $(subdirs)

all: $(subdirs)
$(subdirs):
	@echo building $@
	$(MAKE) -C $@ # -Cは、コマンドを打つ前にそのディレクトリに移動する、という意味
