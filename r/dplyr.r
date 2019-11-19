library(dplyr)

data.result <- iris %>%
  dplyr::filter(Species == "virginica") %>%
  dplyr::arrange(Sepal.Length)
