## renderPlotの中に、reactiveなplotを入れてみる
## 結果は変わらず

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
  titlePanel("title"),
  sidebarLayout(
    sidebarPanel(textOutput("text")), 
    mainPanel(plotOutput("plot"))
  )
)

server <- function(input, output, session){
  output$text <- renderText("This is sidebar")
  
  dat <- reactive(future(downLoadData()))
  plt <- reactive({
    dat() %...>% (function(d)plot(d$x, d$y))
  })

  output$plot <- renderPlot(plt())
}

shinyApp(ui, server)
