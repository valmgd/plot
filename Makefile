.PHONY : make
make :
	./main.sh

.PHONY : get
get :
	./main.sh get

.PHONY : open
open :
	vim main.sh python/main.py python/plot.py R/main.r Makefile
