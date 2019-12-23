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


src_dir = "rstan/6"
model_code = "6_model.stan"
model_bin = "6_model.rds"
if(should_make(model_code, model_bin, src_dir)){
  model <- stan_model(file=file.path(src_dir, model_code))
  saveRDS(model, file=file.path(src_dir, model_bin))
} else {
  cat("skipped compile")
  model <- readRDS(file.path(src_dir, model_bin))
}

stan_fit <- sampling(model, data=dat, verbose=TRUE,
                     iter = ITER, warmup = WARMUP, chains = CHAINS,
                     pars = c("mu_", "sigma1", "sigma2"),
                     cores = 4)

save.image(file=file.path(src_dir, "6.RData"))


