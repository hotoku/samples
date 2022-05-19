HOGE := hoge


hoge:
	@echo hoge


# make -f case.mk hoge => hoge
# make -f case.mk HOGE => エラー
