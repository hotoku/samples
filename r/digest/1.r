library(digest)
library(R6)

A <- R6Class(
  "A",
  public = list(
    x = numeric(0),
    initialize = function(x){
      self$x <- x
    }
  )
)

a1 <- A$new(1)
a2 <- A$new(1)
print(digest(a1))
print(digest(a2))

## R6クラスも、値でhash値を計算可能
