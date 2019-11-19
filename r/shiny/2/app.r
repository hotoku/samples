## ui（fluidPage）にpromiseを入れてみる実験→結論：できない
##
## 入力の選択肢を動的に変化させたいときはどうしたら良いのか・・課題


library(shiny)
library(tidyverse)
library(promises)
library(future)
plan(multiprocess)

downLoadData <- function(){
  Sys.sleep(3)
  tibble(x=1:10, y=1:10)
}

getDataPromise <- function(){
  future(downLoadData())
}

datPrm <- getDataPromise()


getInputX <- function(data){
  selectInput("X", label="X", choices = data$x)
}

ui <- fluidPage(
  sidebarLayout(
    sidebarPanel(
      h1("サンプル"),
      datPrm %...>% getInputX  
    ),
    mainPanel(plotOutput("plot"))
  )
)

server <- function(input, output, session){
  output$plot <- renderPlot({
    datPrm %...>% (function(dat){
      plot(dat$x, dat$y)
    })
  })
}

shinyApp(ui, server)
