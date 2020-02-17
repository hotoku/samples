library(BRugs)
library(R2OpenBUGS)

N <- 100
x.mean <- 3
x.sd <- 1
x <- rnorm(N,x.mean,x.sd)
v <- 1
z <- rnorm(N,0,sqrt(v))

beta1 <- 2
beta2 <- 4
y <- beta1 + beta2*x + z
lm1 <- lm(y ~ x)
summary(lm1)


data1 <- list(y=y, x=x, N=N) 
in1 <- list(beta1=0,beta2=0, S=1) 
inits <- list(in1)
inits

param <- c("beta1","beta2","S") 
file.name <- "lm1.txt"
model1 <- file.name
bugs1 <- bugs(data1, inits, param, model.file=model1, 
              n.chains=1, n.iter=300, n.burnin=100, n.thin=2, 
              working.directory = "bugs/1",
              OpenBUGS.pgm = "/usr/local/bin/OpenBUGS")
