all: $(subst .csv,.done,$(shell ls *.csv))

%.done: %.csv
	touch $@
