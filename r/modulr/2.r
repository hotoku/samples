library(modulr)

car_provider <- function(engine, wheel){
  list(
    run=function(){
      engine$run()
      wheel$run()
    }
  )
}

"wheel_impl_1" %provides% {
  list(
    run=function(){
      print("wheel 1")
    }
  )
}

"engine_impl_1" %provides% {
  list(
    run=function(){
      print("engine 1")
    }
  )
}

"car" %requires% list(
  engine="engine",
  wheel="wheel"
) %provides% car_provider

"wheel" %requires% list(
  impl="wheel_impl_1"
) %provides% {
  impl
}

"engine" %requires% list(
  impl="engine_impl_1"
) %provides% {
  impl
}

car <- make("car")
car$run()
