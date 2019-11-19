f <- function(){
    print(sys.frame())          
    print(parent.frame())
}

f()

f2 <- function(){
    function(){
        print(sys.frame())          
        print(parent.frame())
    }
}

f2()()
