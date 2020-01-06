library(R6)

A <- R6Class(
  "A",
  public = list(
    x = NULL,
    initialize = function(x){
      self$x <- x
    }
  )
)

a <- A$new(100)
print(a$x)

f <- function(a, x) {
  a$x <- x
}

f(a, 200)
print(a$x) # R6クラスは参照渡しなので中身が更新されている
