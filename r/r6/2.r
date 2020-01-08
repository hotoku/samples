library(R6)

A <- R6Class(
  "A",
  public = list(
    x = NULL,
    z = NULL,
    initialize = function(x){
      self$x <- x
    }
  )
)

a <- A$new(100)
# a$y <- 10 これはエラー
a$z <- 10 # これはOK