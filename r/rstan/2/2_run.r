library(rstan)
library(tidyverse)

set.seed(101)

ITER <- 5e4
WARMUP <- 1e4
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

model <- stan_model(file="rstan/2/2_model.stan")
stan_fit <- sampling(model, data=dat, verbose=TRUE,
                     iter = ITER, warmup = WARMUP, chains = CHAINS,
                     cores = 4)

save.image(file="2.RData")
