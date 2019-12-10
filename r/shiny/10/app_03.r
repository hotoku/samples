## reactiveにしてみる
## reactiveにしてみても、やはりdownloadDataが終わるまで描画がブロックされる


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
  
  dat <- reactiveVal(downLoadData())

  output$plot <- renderPlot({
    plot(dat()$x, dat()$y)
  })
}

shinyApp(ui, server)
