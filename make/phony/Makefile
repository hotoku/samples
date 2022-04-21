all: target.view
	@echo "making all: $@ <- ($^)"


# パターン1:
# .PHONY: target.view
# target.view: target.sql
# -> 実行される: target.viewファイルではないが、直にターゲットとして指定されているので、それは実行する
#
# パターン2:
# .PHONY: target.view
# %.view: %.sql
# -> 実行されない: target.viewがファイルではないので、直にターゲットとして指定されていなければ作ろうとしない
#
# パターン3:
# %.view: %.sql
# -> 実行される: target.viewがファイルなので、存在しなければ作ろうとする。
# 直にターゲットとして指定されていなければ、パターンマッチルールで当てはまるものを探す。
%.view: %.sql
	@echo "making view: $@ <- ($^)"
	@cp $< $@
	@echo "this is view" >> $@


%.sql:
	@echo "making sql: $@ <- ($^)"
	@echo "this is sql" >> $@


.PHONY: clean
clean:
	ls | grep -v Makefile | xargs rm -f
