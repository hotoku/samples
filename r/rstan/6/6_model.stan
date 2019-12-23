data {
  int N;
  real Y[N];
}

parameters {
  real mu[N];
  real<lower=0> sigma1;
  real<lower=0> sigma2;
}

model {
  for(t in 3:N){
    mu[t] ~ normal(2*mu[t-1] - mu[t-2], sigma2);    
  }
  for(t in 1:N){
    Y[t] ~ normal(mu[t], sigma1);
  }
}

generated quantities {
  real mu_[3];
  mu_[1] = mu[1];
  mu_[2] = mu[N/2];
  mu_[3] = mu[N];
}
