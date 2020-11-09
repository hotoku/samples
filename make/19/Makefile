HOGE := hoge
FUGA := FUGA
export FUGA


all: with without env subsub


with:
	@echo ===
	@echo with
	@$(MAKE) HOGE=$(HOGE) -C sub


without:
	@echo ===
	@echo without
	@$(MAKE) -C sub


env:
	@echo ===
	@echo env
	@export HOGE=$(HOGE)
	@$(MAKE) -C sub


subsub:
	@echo ===
	@echo subsub
	@$(MAKE) -C sub subsub


# 結論
# - 変数は引き継がれない
# - 環境変数も引き継がれない
# - Make自体のexport構文を使う
# - 直下だけではなく、もっと下のディレクトリにも引き継がれる
