rm(list=ls(all=T))
f2 <- function(){
  source("source/1.r", local=TRUE)
  f()
}
f2()
ls()
# local=TRUEとすれば、呼び出した環境の中に読み込まれる