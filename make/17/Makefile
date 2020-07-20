t1:
# これはOK
	if [ -z "" ]; then echo empty; fi

t2:
# これはNG
	if [ -z "" ]; then 
		echo empty
	fi

t3:
# これはOK
# emptyの後ろの;がないとエラー
	if [ -z "" ]; then\
		echo empty;\
	fi
