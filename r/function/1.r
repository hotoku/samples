f <- function(x){x + 1}
g <- function(){}

# これはダメ
# args(g) <- args(f)

g <- function(x){}
body(g) <- body(f)
g(10)
