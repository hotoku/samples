getCounter <- function(){
  n <- 0
  counter <- function(){
    n <<- n + 1
    n
  }
  counter
}

cnt <- getCounter()
cnt()
cnt()
cnt()
