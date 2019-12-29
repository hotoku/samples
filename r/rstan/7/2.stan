// 普通の方法でサンプリング

data {
  int N;
  vector[N] Y;
}

parameters {
  vector[N] s;
  real<lower=0> sigma1;
  real<lower=0> sigma2;
}

model {
  for(i in 3:N){
    s[i] ~ normal(2*s[i-1] - s[i-2], sigma1);
  }
  for(i in 1:N){
    Y[i] ~ normal(s[i], sigma2);
  }
}
