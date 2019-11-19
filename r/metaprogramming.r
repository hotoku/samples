library(tidyverse)
library(stringr)


## substituteで評価前の式を取得
summarise_by <- function(dat, key, val){
    k <- as.character(substitute(key))
    v <- as.character(substitute(val))
    "dat __PIPE__
        group_by(%s) __PIPE__
        summarise(%s = sum(%s)) __PIPE__
        ungroup" %>%
        sprintf(k, v, v) %>%
        str_replace_all("__PIPE__", "%>%") %>%
        parse(text = .) %>%
        eval
}

tibble(x=1:10, y=rep(1:2,5)) %>%
    summarise_by(key = y, val = x)



## evalq(exp)で呼び出し元の環境で実行
f <- function(){
    one_time_connection(con)
}

one_time_connection <- function(obj){
    var <- as.character(substitute(obj))
    ex <- "
%s <- get_connection();
on.exit(disconnect(%s))
" %>% sprintf(var, var) %>%
      parse(text = .)
    eval(ex, env = parent.frame())
}

get_connection <- function(){
    print("get_connection")
}

disconnect <- function(x){
    print("disconnect")
}

f()
