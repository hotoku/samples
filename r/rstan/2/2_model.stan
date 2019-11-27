data {
  int NUM_DATA;
  int NUM_CLASS;
  int<lower=1, upper=NUM_CLASS> CLASS[NUM_DATA];
  real Y[NUM_DATA];
}

parameters {
  real m;
  real mu[NUM_CLASS];
  real<lower=0> sigma1;
  real<lower=0> sigma2;
}

model {
  for(i in 1:NUM_CLASS){
    mu[i] ~ normal(m, sigma2);
  }
  for(i in 1:NUM_DATA){
    Y ~ normal(mu[CLASS[i]], sigma1);
  }
}

