library(ggplot2)

dat <- tibble(x=1:10, y=1:10)

f <- function(g, path){
  pdf(path)
  on.exit(dev.off())
  print(g)
}

g <- dat %>% ggplot(aes(x,y)) + geom_point()
f(g, "temp.pdf")
