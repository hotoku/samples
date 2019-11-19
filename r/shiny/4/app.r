# データの再読み込みの例

library(shiny)
library(tidyverse)
library(httr)
library(loggit)




downLoadData <- function(){
  # 現在時刻を返してくれるAPI
  url <- "https://ntp-a1.nict.go.jp/cgi-bin/json"
  ret <- GET(url) %>% content
  ret$st
}

dat <- reactiveVal(downLoadData())

ui <- fluidPage(
  actionButton("refresh", "Refresh"),
  textOutput("time")
)

server <- function(input, output, session){
  observeEvent(input$refresh, {
    dat(downLoadData())
  })
  output$time <- renderText(dat())
}

shinyApp(ui, server)
