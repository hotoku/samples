rm(list=ls(all=T))

library(rstan)
library(loggit)
library(ggmcmc)
library(tidyverse)
loggit::setLogFile("rstan/7/1.json")


do.log <- function(lvl, msg){
  msg2 <- sprintf("%s: %s", Sys.time(), msg)
  loggit(lvl, msg2)
}

log.info <- function(msg){ do.log("INFO", msg) }
log.debug <- function(msg){ do.log("DEBUG", msg) }

compile <- function(src){
  cache <- sprintf("%s.cache", src)
  if(!file.exists(cache) || file.mtime(cache) < file.mtime(src)){
    log.info("compiling")
    model <- stan_model(file = src)
    saveRDS(model, file = cache)
  } else {
    log.info("reading cache")
    model <- readRDS(cache)
  }
  model
}

   

src_dir <- "rstan/7"
dat <- read_csv(file.path(src_dir, "dat.csv"))
design_matrix <- read_csv(file.path(src_dir, "dm.csv"))

stan_code <- file.path(src_dir, "1.stan")
model <- compile(stan_code)


log.info("sampling start")
stan_fit <- sampling(model, verbose = TRUE,
                     iter = 5e3, 
                     warmup = 1e3, 
                     chains = 4,
                     cores = 4,
                     data = list(
                       N=nrow(dat),
                       Y=dat$sales,
                       X=design_matrix$全体
                     ))
log.info("sampling end")

# INFO: 2019-12-26 14:55:11: sampling start
# INFO: 2019-12-26 15:05:21: sampling end


# 5,000サンプル
# INFO: 2019-12-29 01:57:35: sampling start
# INFO: 2019-12-29 02:11:46: sampling end


saveRDS(stan_fit, file=file.path(src_dir, "1_fit.rds"))

stan_fit <- readRDS(file=file.path(src_dir, "1_fit.rds"))
ex <- rstan::extract(stan_fit, c("s", "mu"))
smpl <- ggs(stan_fit, stan_include_auxiliar = TRUE)

plot(dat$sales, ty="l")
lines(colMeans(ex$s), col=2)

plot(dat$sales, ty="l")
lines(colMeans(ex$mu), col=2)

# 5,000サンプルでは全然収束してない

ex2 <- rstan::extract(stan_fit, "s", inc_warmup=T)
plot(ex2$s[1:4000,1], ty="l")
