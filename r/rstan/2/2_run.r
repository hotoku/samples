library(rstan)
library(tidyverse)

rm(list=ls(all=T))
source("utils.r")

set.seed(101)

ITER <- 2e3
WARMUP <- 5e2
CHAINS <- 4

NUM_DATA <- 1000
NUM_CLASS <- 3

CLASS <- sample(1:NUM_CLASS, NUM_DATA, replace = TRUE)

sigma1 <- 1
sigma2 <- 10

m <- 0;
mu <- rnorm(NUM_CLASS, m, sigma2)

Y <- rnorm(NUM_DATA, mu[CLASS], sigma1)

dat <- list(
  NUM_DATA=NUM_DATA,
  NUM_CLASS=NUM_CLASS,
  CLASS=CLASS,
  Y=Y
)

src_dir = "rstan/2"
model_code = "2_model.stan"
model_bin = "2_model.rds"
if(should_make(model_code, model_bin, src_dir)){
  model <- stan_model(file=file.path(src_dir, model_code))
  saveRDS(model, file="2_model.rds")
} else {
  cat("skipped compile")
  model <- readRDS(file.path(src_dir, model_bin))
}
stan_fit <- sampling(model, data=dat, verbose=TRUE,
                     iter = ITER, warmup = WARMUP, chains = CHAINS,
                     cores = 4)

save.image(file=file.path(src_dir, "2.RData"))
