# 滑らかにaからbまで変化する関数を定義する

f1 <- function(x){
  1/(1+exp(-x))
}

x <- seq(-10, 10, length.out = 100)
plot(x, f1(x), ty="l")

f2 <- function(x, a, b){
  (b-a) * f1(x) + a
}

plot(x, f2(x, .5, 3), ty="l")

f3 <- function(x, a, b, slope, pos){
  f2(slope*(x-pos), a, b)
}
plot(x, f3(x, 0.5, 3, 1, 0), ty="l")
lines(x, f3(x, 0.5, 3, 0.3, 0), col=2)
lines(x, f3(x, 0.5, 3, 3, 0), col=3)
lines(x, f3(x, 0.5, 3, 3, 3), col=4)
lines(x, f3(x, 0.5, 3, -1, 3), col=5)


plot(x, f3(x, -1, -3, 1, 0), ty="l")


plot(x, f3(x, -3, -1, 1, 0), ty="l")
