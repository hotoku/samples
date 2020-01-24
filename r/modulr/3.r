library(modulr)
library(R6)

build <- function(conf){
  "a" %requires% list(
    impl = conf$impl
  ) %provides% {
    obj <- a$new(conf$id)
    obj$inject(impl)
  }
  "b" %provides% { 
    b$new()
  }
  "c" %provides% {
    c$new()
  }
}

a <- R6Class(
  "a",
  public = list(
    id = NULL,
    impl = NULL,
    initialize = function(id){
      self$id = id
    },
    inject = function(impl){
      self$impl <- impl
      self
    },
    run = function(){
      self$impl$run()
    }
  )
)

b <- R6Class(
  "b",
  public = list(
    run = function(){
      "b"
    }
  )
)

c <- R6Class(
  "c",
  public = list(
    run = function(){
      "c"
    }
  )
)
build(list(id=1, impl="b"))
a1 <- make("a")
a1$run()

build(list(id=2, impl="c"))
a2 <- make("a")
a2$run()
