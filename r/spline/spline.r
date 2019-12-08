library(splines)
library(mgcv)

x <- 1:100
knots <- seq(min(x), max(x), length.out = 10)

## 普通のspline
B <- bs(x, knots = knots,
        degree = 3, intercept = FALSE)

plot(B[,1], ty="l")
for(i in 1:ncol(B)){
  lines(B[,i], col=i)
}


## 周期spline
B2 <- cSplineDes(x, knots = knots, ord = 4)

plot(B2[,1], ty="l")
for(i in 1:ncol(B2)){
  lines(B2[,i], col=i)
}


## 周期splineの適当なサンプルをプロットしてみる
a <- matrix(
  rnorm(ncol(B2) * 3),
  nrow=ncol(B2)
)

vals <- B2 %*% a
plot(vals[,1], ty="l")
for(i in 2:ncol(vals)){
  lines(vals[,i], col=i)
}
