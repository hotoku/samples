rm(list=ls(all=T))

try.until.success <- function(f, ...){
    got.it <- TRUE
    ret <- 100
    NG <- function(e){
        got.it <<- FALSE
    }
    OK <- function(v){
        ret <<- v
        got.it <<- TRUE
    }
    repeat{
        tryCatch({
            OK(f(...))
        },
        error = function(e){
            print(e)
            NG()
        })
        if(got.it){
            break
        }
    }
    ret
}


n <- 0
f <- function(){
    n <<- n + 1
    if(n < 10) stop(n)
    n
}


x <- try.until.success(f)
