f <- function(){
    on.exit(print(1))
    on.exit(print(2))
}
f()

g <- function(){
    on.exit(print(1))
    on.exit(print(2), TRUE)
}
g()
    
