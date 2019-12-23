subdirs := a b

.PHONY: all $(subdirs)

all: $(subdirs)
$(subdirs):
	$(MAKE) -C $@ # -Cは、コマンドを打つ前にそのディレクトリに移動する、という意味
