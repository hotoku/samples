## futureに包んでみる
## .... 結局、3秒待たされるぞ・・。
## そういうものっぽい
## https://blog.rstudio.com/2018/06/26/shiny-1-1-0/
## shinyの公式blog。asyncをサポートした時のアナウンス。
## 解決したいのは1セッションの中でのブロッキングではなくて、
## 1プロセスの中での複数セッションのブロッキング
## （複数のユーザーが、同一プロセスのshinyサーバーに接続するなど)
## 1セッションの中でのブロックを何とかするなら、reactiveを使う、多分。




library(shiny)
library(tidyverse)
library(promises)
library(future)
plan(multiprocess)

downLoadData <- function(){
  Sys.sleep(10)
  tibble(x=1:10, y=1:10)
}

ui <- fluidPage(
  fluidRow(textOutput("text")),
  fluidRow(plotOutput("plot"))
)

server <- function(input, output, session){
  output$text <- renderText("This is Header")
  output$plot <- renderPlot({
    future({downLoadData()}) %...>%
      (function(dat){
        plot(dat$x, dat$y)
      })
  })
}

shinyApp(ui, server)
