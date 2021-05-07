all: var
	@echo before eval
	$(eval hoge := $(shell read -p "answer: " var && echo $$var))
	@echo after eval
	@echo hoge = $(hoge)

var:
	@echo "input please"
