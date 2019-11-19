# UIをダイナミックにする例

library(shiny)
library(tidyverse)
library(httr)
library(loggit)




downLoadData <- function(){
  # 現在時刻を返してくれるAPI
  url <- "https://ntp-a1.nict.go.jp/cgi-bin/json"
  ret <- GET(url) %>% content
  ret$st %>% as.integer
}

ui <- fluidPage(
  actionButton("refresh", "Refresh"),
  htmlOutput("select"),
  textOutput("text")
)

server <- function(input, output, session){
  dat <- reactiveVal(downLoadData())
  observeEvent(input$refresh, {
    dat(downLoadData())
  })
  output$select <- renderUI({
    selectInput("select", "選択", choices = c(dat(), dat() + 1, dat() + 2))
  })
  output$text <- renderText(input$select)
}

shinyApp(ui, server)
