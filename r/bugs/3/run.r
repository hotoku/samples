library(BRugs)
library(stringr)

model_file <- "bugs/3/model.txt"
dat <- list(
  z = 0,
  tau = 1e2
)  
n_chain = 1
n_iter = 1e6
burnin = 0.1
n_thin = 1e2

modelCheck(model_file)
data_file <- bugsData(dat, digits = 10)
modelData(data_file)
modelCompile(n_chain)
modelGenInits()
modelUpdate(n_iter * burnin)
samplesSet(str_split("x,y", ",")[[1]])
samplesSetThin(n_thin)  
modelUpdate(n_iter)

xs <- samplesSample("x")
ys <- samplesSample("y")

plot(xs, ys)
cor(xs, ys)
