library(rstan)
library(tidyverse)

rm(list=ls(all=T))
source("utils.r")

ITER <- 4e3
WARMUP <- 1e3
CHAINS <- 4

## データ作成

N <- 200
x <- 1:N
mu <- sin(2 * pi * (x/N))
sigma1 <- 0.1
Y <- mu + rnorm(N, sd=sigma1)

plot(Y, ty="l")
lines(mu, col=2)


dat <- list(
  N=N,
  Y=Y
)


src_dir = "rstan/5"
model_code = "5_model.stan"
model_bin = "5_model.rds"
if(should_make(model_code, model_bin, src_dir)){
  model <- stan_model(file=file.path(src_dir, model_code))
  saveRDS(model, file=file.path(src_dir, model_bin))
} else {
  cat("skipped compile")
  model <- readRDS(file.path(src_dir, model_bin))
}

stan_fit <- sampling(model, data=dat, verbose=TRUE,
                     iter = ITER, warmup = WARMUP, chains = CHAINS,
                     pars = c("mu[1]", sprintf("mu[%d]", N%/%2), sprintf("mu[%d]", N)), 
                     # この書き方だと、
                     # no parameter mu[1], mu[100], mu[200]; sampling not done
                     # here are whatever error messages were returned
                     # というメッセージが出て何もサンプリングされない。
                     # stanファイルの中で、明示的に残すパラメータを別名をつけた方が良さそう
                     cores = 4)

save.image(file=file.path(src_dir, "4.RData"))


