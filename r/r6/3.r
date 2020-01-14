library(R6)

# privateの使い方 

A <- R6Class(
  "A",
  private = list(
    x=1
  ),
  public = list(
    initialize = function(x){
      private$x <- x
    },
    print = function(){
      print(private$x)
    }
  )
)

a <- A$new(100)
a$print()
