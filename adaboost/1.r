library(tidyverse)


entropy <- function(p){
  if(p==0 || p==1) return(0)
  -p * log(p) - (1-p) * log(1-p)
}

# yを交差エントロピーの意味で最もよく分類するx0を出力する
# 決定境界は、x <= x0 → y=0 /  x > x0 → y= 1（あるいはその逆）という意味で使う
decision_stump_1 <- function(x, y){
  m <- min(x)
  M <- max(x)
  if(unique(y) %>% length == 1) return(M)
  od <- order(x)
  x2 <- x[od]
  y2 <- y[od]
  n <- length(x)
  es <- numeric(n)
  for(i in 1:n){
    n1 <- sum(y2[1:i] == 1)
    n2 <- if(i < n) sum(y2[(i+1):n] == 1) else 0
    p1 <- n1 / i
    p2 <- if(i < n) n2 / (n-i) else 0
    es[i] <- entropy(p1) + entropy(p2)
  }
  pos <- which(es==min(es))[1]
  threshold <- x2[pos]
  n1 <- sum(y2[1:pos] == 1)
  n2 <- sum(y2[1:pos] == 0)
  val1 <- if(n1 > n2) 1 else 0
  val2 <- if(val1 == 1) 0 else 1
  pred <- function(x){
    ifelse(x <= threshold, val1, val2)
  }
  list(threshold=threshold, loss=es[pos], pred=pred)
}

decision_stump <- function(x, y){
  nc <- ncol(x)
  threshold <- numeric(nc)
  loss <- numeric(nc)
  pred <- as.list(rep(NA, nc))
  for(i in 1:nc){
    ret <- decision_stump_1(x[,i], y)
    threshold[i] <- ret$threshold
    loss[i] <- ret$loss
    pred[[i]] <- ret$pred
  }
  col <- which(loss==min(loss))[1]

  ret <- function(x){
    pred[[col]](x[,col])
  }
  ret
}

x <- matrix(rnorm(40), ncol=2)
y <- x[,2] >= -x[,1]
# y <- as.numeric(x[,2] <= 0)

f <- decision_stump(x, y)


dat <- tibble(x1=x[,1], x2=x[,2], y=y, pred=f(x))
ggplot(dat, aes(x=x1, y=x2)) +
  geom_point(aes(color=y+1)) + scale_color_identity() +
  geom_point(aes(shape=pred)) + scale_shape_identity()
