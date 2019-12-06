library(rstan)
library(tidyverse)
library(ggmcmc)

rm(list=ls(all=T))
source("utils.r")

load("rstan/4/4.RData")


get_ggs <- function(stan_fit, par_name, inc_warmup){
  iter <- stan_fit@stan_args[[1]]$iter
  warmup <- stan_fit@stan_args[[1]]$warmup
  n_chains <- stan_fit@stan_args %>% length
  path <- extract(stan_fit, par_name,
                  inc_warmup=inc_warmup,
                  permuted=T)[[par_name]]
  num_step <- if(inc_warmup) iter else iter-warmup
  iteration <- rep(1:num_step, n_chains)
  chain <- Reduce(c, Map(function(n)rep(n, num_step), 1:n_chains))
  dat <- tibble(Iteration=as.double(iteration),
         Chain=as.integer(chain),
         Parameter=as.factor(par_name),
         value=path)
  attributes(dat)$nParameters <- 1
  attributes(dat)$nChains <- n_chains
  dat
}

tib <- ggs(stan_fit, family="mu")
ggmcmc(tib)


dat <- get_ggs(stan_fit, c("sigma1", "mu[1]"), FALSE)
ggmcmc(dat, file="rstan/4/4_ggmcmc.pdf")

par_name <- "sigma1"
inc_warmup <- FALSE
path <- extract(stan_fit, par_name,
                inc_warmup=inc_warmup,
                permuted=T)

if(inc_warmup){
  
}

dat <- tibble(
  Iteration=rep(1:iter)    
)
