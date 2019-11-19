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

ui <- fluidPage(
  sidebarLayout(
    sidebarPanel(h1("サンプル")),
    mainPanel(plotOutput("plot"))
  ))

server <- function(input, output, session){
  output$plot <- renderPlot({
    datPrm %...>% (function(dat){
      plot(dat$x, dat$y)
    })
  })
}

shinyApp(ui, server)
