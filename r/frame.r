f <- function(){
    evalq({
        z <- 123
    }, env = parent.frame())
}

g <- function(){
    f()
    z
}

g()
