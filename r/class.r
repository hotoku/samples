f.cls1 <- function(y, a){
    print("cls1")
    print(a)
}

f.cls2 <- function(z, b){
    print("cls2")
    print(b)
}


x1 <- structure(1, class="cls1")
x2 <- structure(2, class="cls2")


f <- function(x, ...){
    UseMethod("f", x)
}

f(x1, 100)
f(x2, "a")
