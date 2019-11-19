f <- function(){
    browser()
}

## browser()の中で、以下を実行するとエラー
if(TRUE){
    x <- 1    
}
print(x)
