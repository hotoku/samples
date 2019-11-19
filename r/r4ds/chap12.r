library(tidyverse)


stocks <- tibble(
  year   = c(2015, 2015, 2016, 2016),
  half  = c(   1,    2,     1,    2),
  return = c(1.88, 0.59, 0.92, 0.17)
)


stocks %>% 
  spread(year, return)

stocks %>% 
    spread(year, return) %>%
    gather("year", "return", `2015`:`2016`)
## 一見、元に戻るように思うが、yearの型が違う


stocks %>% 
    spread(year, return) %>%
    gather("year", "return", `2015`:`2016`, convert = T)
## convertすると、文字列から自動変換してくれる(が、intに変わってしまうので元には戻らない)


table4a %>%
    gather(1999, 2000, key = "year", value = "cases")
## エラー: 1999, 2000が、列名ではなく列番号と解釈される



people <- tribble(
  ~name,             ~key,    ~value,
  #-----------------|--------|------
  "Phillip Woods",   "age",       45,
  "Phillip Woods",   "height",   186,
  "Phillip Woods",   "age",       50,
  "Jessica Cordero", "age",       37,
  "Jessica Cordero", "height",   156
)
people %>%
    spread(key, value)
## エラー: Phillip Woods, age: が2個できるので
