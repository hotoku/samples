rm(list=ls(all=T))
f2 <- function(){
  source("source/1.r")
  f()
}
f2()
ls()
# 関数の中でsourceをしても、グローバル環境に読み込まれる