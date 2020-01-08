rm(list=ls(all=T))

library(rstan)
library(loggit)
library(ggmcmc)
library(tidyverse)
loggit::setLogFile("rstan/7/3.json")


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

A_ <- function(N){
  ret <- matrix(0, nrow=N, ncol=N)
  ret[1,1] <- ret[2,2] <- 1
  for(i in 3:N){
    ret[i,1] <- -i + 2
    for(j in 2:i){
      ret[i,j] <- i - j + 1
    }
  }
  ret
}

Sl_ <- function(N){
  A <- A_(N)
  AAt <- A %*% t(A)
  eg <- eigen(AAt)
  vl <- eg$values
  vc <- eg$vectors
  vc %*% diag(vl^0.5)
}


src_dir <- "rstan/7"
dat <- read_csv(file.path(src_dir, "dat.csv"))
design_matrix <- read_csv(file.path(src_dir, "dm.csv"))

stan_code <- file.path(src_dir, "3.stan")
model <- compile(stan_code)

N <- nrow(dat)
Sl <- Sl_(N)

log.info("sampling start")
stan_fit <- sampling(model, verbose = TRUE,
                     iter = 5e3, 
                     warmup = 1e3, 
                     chains = 4,
                     cores = 4,
                     data = list(
                       N=N,
                       Y=dat$sales,
                       X=design_matrix$全体,
                       Sl=Sl
                     ))
log.info("sampling end")



saveRDS(stan_fit, file=file.path(src_dir, "3_fit.rds"))

stan_fit <- readRDS(file=file.path(src_dir, "3_fit.rds"))
ex <- rstan::extract(stan_fit, c("s", "mu"))
smpl <- ggs(stan_fit, stan_include_auxiliar = TRUE)

plot(dat$sales, ty="l")
lines(colMeans(ex$s), col=2)

plot(dat$sales, ty="l")
lines(colMeans(ex$mu), col=2)

