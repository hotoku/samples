library(R6)

# 継承の例


A <- R6Class(
  "A",
  public = list(
    x = NULL,
    initialize = function(x){
      self$x <- x
    },
    f = function(){
      self$x
    }
  )
)

B <- R6Class(
  "B",
  inherit = A, # Aを継承する
  public = list(
    f = function(){ # fを上書き
      self$x + 1
    }
  )
)

a <- A$new(100)
b <- B$new(100)
print(a$f()) # => 100
print(b$f()) # => 101
