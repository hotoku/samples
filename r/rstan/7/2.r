rm(list=ls(all=T))

library(rstan)
library(loggit)
library(ggmcmc)
library(tidyverse)
loggit::setLogFile("rstan/7/2.json")


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

stan_code <- file.path(src_dir, "2.stan")
model <- compile(stan_code)


log.info("sampling start")
stan_fit <- sampling(model, verbose = TRUE,
                     iter = 5e4, 
                     warmup = 1e4, 
                     chains = 4,
                     cores = 4,
                     data = list(
                       N=nrow(dat),
                       Y=dat$sales,
                       X=design_matrix$全体
                     ))
log.info("sampling end")

# INFO: 2019-12-26 15:42:27: sampling start
# INFO: 2019-12-26 15:51:54: sampling end

saveRDS(stan_fit, file=file.path(src_dir, "2_fit.rds"))

ex <- rstan::extract(stan_fit)
smpl <- ggs(stan_fit, stan_include_auxiliar = TRUE)

plot(dat$sales, ty="l")
lines(colMeans(ex$s), col=2)


ex2 <- rstan::extract(stan_fit, "s", inc_warmup=T)
plot(ex2$s[1:10000,1], ty="l")
for(i in 1:3){
  lines(ex2$s[(1:10000)+i*5e4, 1], col=i+1)
}

# 5000サンプルで十分収束している