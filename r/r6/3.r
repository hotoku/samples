library(R6)

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
