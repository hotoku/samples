## reactiveとfutureを組み合わせる
## これでもまだ、「バックグラウンドでデータ準備 + 即描画」は実現してない
## https://rstudio.github.io/promises/articles/casestudy.html
## このページが参考になりそう


library(shiny)
library(tidyverse)
library(promises)
library(future)
plan(multiprocess)

downLoadData <- function(){
  cat("download start\n")
  Sys.sleep(10)
  cat("download end\n")
  tibble(x=1:10, y=1:10)
}

ui <- fluidPage(
  fluidRow(textOutput("text")),
  fluidRow(plotOutput("plot"))
)

server <- function(input, output, session){
  output$text <- renderText("This is Header")
  
  dat <- reactive(future(downLoadData()))

  output$plot <- renderPlot({
    dat() %...>% (function(d)plot(x=d$x, y=d$y))
  })
}

shinyApp(ui, server)
