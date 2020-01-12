if_not_null <- function(val, default=NULL){
  if(!is.null(val)){
    val
  } else {
    default
  }
}

if_not_null(1) %>%
  if_not_null(10) %>%
  if_not_null(stop("value is not set")) # => 1
  
if_not_null(NULL) %>%
  if_not_null(10) %>%
  if_not_null(stop("value is not set")) # => 10

if_not_null(NULL) %>%
  if_not_null(NULL) %>%
  if_not_null(stop("value is not set")) # error
