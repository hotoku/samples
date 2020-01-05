library(docopt)

"Usage: docopt.r [-h] [--opt1 OPT1] ARG1 ARG2

-h --help   show this
--opt1 OPT1 option 1
ARG1        arg 1
ARG2        arg 2 
" -> doc


docopt(doc, "--opt1 XXX a b")

docopt(doc, "XXX YYY") # エラー
# opt1がオプショナルになってない..
# 2.rmdで解決した

# 実際の引数をparseするときはこっち
# docopt(doc) 


