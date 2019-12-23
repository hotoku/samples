subdirs := a b

.PHONY: all $(subdirs)

all: $(subdirs)
$(subdirs):
	make -C $@ # -Cは、コマンドを打つ前にそのディレクトリに移動する、という意味
