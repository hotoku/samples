# 配列を使って、複数のレシピをマクロによって定義する例
WORDS := a b c d e f g h i j


define recipe
.PHONY: $1
$1:
	@echo $$@
endef


all: $(WORDS)


# callするだけだと文字列を作るだけなのでevalすること
$(foreach word,$(WORDS),$(eval $(call recipe,$(word))))
