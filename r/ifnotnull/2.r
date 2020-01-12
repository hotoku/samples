if_not_null <- function(val, default=NULL){
  if(!is.null(val)){
    val
  } else {
    default
  }
}

mystop <- function(msg){
  stop(msg)
}

if_not_null(1) %>%
  if_not_null(l1$val) # => 1

if_not_null(1) %>%
   if_not_null(stop("val is not set")) # 1

if_not_null(NULL) %>%
  if_not_null(10)

if_not_null(NULL) %>%
  if_not_null(stop("val is not set"))
