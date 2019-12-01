## rstanの出力に保存されるサンプルパスを一部のパラメータに制限したい
## 結論。配列パラメータの一部部のみを保存することはできなかった

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


src_dir = "rstan/3"
model_code = "3_model.stan"
model_bin = "3_model.rds"
if(should_make(model_code, model_bin, src_dir)){
  model <- stan_model(file=file.path(src_dir, model_code))
  saveRDS(model, file=file.path(src_dir, model_bin))
} else {
  cat("skipped compile")
  model <- readRDS(file.path(src_dir, model_bin))
}

stan_fit <- sampling(model, data=dat, verbose=TRUE,
                     iter = ITER, warmup = WARMUP, chains = CHAINS,
                     pars = c("sigma1", "sigma2", "mu"),
                              ## "mu[1]", sprintf("mu[%d]", N%/%2), sprintf("mu[%d]", N)),
                     cores = 4)

save.image(file=file.path(src_dir, "3.RData"))


