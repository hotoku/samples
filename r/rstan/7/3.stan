// 主成分分解してサンプリング

data {
  int N;
  vector[N] Y;
  vector[N] X; 
  matrix[N,N] Sl;
}

parameters {
  vector[N] eta;
  real c;
  real<lower=0> sigma1;
  real<lower=0> sigma2;
}

transformed parameters {
  vector[N] s;
  vector[N] mu;
  s = Sl * eta;
  mu = s + c * X;
}

model {
  eta ~ normal(0, sigma1);
  Y ~ normal(mu, sigma2);
}
