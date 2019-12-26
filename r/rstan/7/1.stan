# 普通の方法でサンプリング

data {
  int N;
  vector[N] Y;
  vector[N] X;
}

parameters {
  vector[N] s;
  real c;
  real<lower=0> sigma1;
  real<lower=0> sigma2;
}

transformed parameters {
  vector[N] mu;
  mu = s + c * X;
}

model {
  for(i in 3:N){
    s[i] ~ normal(2*s[i-1] - s[i-2], sigma1);
  }
  Y ~ normal(mu, sigma2);
}
