should_make <- function(src, prod, dir){
  files <- system(sprintf("ls --sort=time %s", dir), intern = TRUE)
  if(!any(files == src)){
    stop(sprintf("%s does not exist in %s", src, dir))
  }
  if(!any(files == prod)){
    return(TRUE)
  } else {
    pos_src = which(src==files)
    pos_prod = which(prod==files)
    return(pos_src <= pos_prod)
  }
}
