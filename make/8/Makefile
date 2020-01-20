.PHONY: all


VAR = "var $1 $2" # 変数も引数を持つことができる

define MACRO # マクロを定義できる
	@echo macro $1 $2
endef


all:
	@echo $(call VAR,a,b) # callで変数に引数を渡せる
	$(call MACRO,c,d)     # callでマクロに引数を渡せる
