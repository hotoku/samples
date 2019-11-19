library(tidyverse)

x <- tibble(x=1:10) %>%
    rename(y = x)
