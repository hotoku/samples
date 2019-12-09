library(future)
library(promises)
plan(multiprocess)

wait_return <- function(t, v){
  Sys.sleep(t)
  v
}

x1 <- wait_return(2, 1)
print(x1)
print(Sys.time())
x2 <- wait_return(2, 1)
print(x1)
print(Sys.time())


future(wait_return(2, 1)) %...>% print
print(Sys.time())
future(wait_return(2, 1)) %...>% print
print(Sys.time())
