# reactiveの使い方の例。その2
# reactiveは、「変化し得る値」を受け取って、「値が変化したときだけ再計算する」機能を提供。
# reactiveValは、reactiveと名前が似ているけど役割は別モノで、上の文章でいう「変化し得る値」
# を表現するモノ。
# reactiveは、「値の変化」というイベントを受け取る側で、reactiveValはイベントを送る方。

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

getText <- function(time, radio, text){
  txt <- sprintf("time=%s radio=%s text=%s",
                 time, radio, text)
  loggit("INFO", txt)
  txt
}

ui <- fluidPage(
  fluidRow(
    column(4, actionButton("refresh", "Refresh")),
    column(4, radioButtons("radio1", "Radio 1", choices = 1:3)),
    column(4, radioButtons("radio2", "Radio 2", choices = 4:6))
  ),
  fluidRow(
    column(6, textOutput("text1")),
    column(6, textOutput("text2"))
  )
)


dat <- reactiveVal(downLoadData())
server <- function(input, output, session){
  observeEvent(input$refresh, {
    dat(downLoadData())
  })
  text1 <- reactive({
    getText(dat(), input$radio1, "text1")
  })
  text2 <- reactive({
    getText(dat(), input$radio2, "text2")
  })
  output$text1 <- renderText(text1())
  output$text2 <- renderText(text2())
  output$time <- renderText(dat())
}

shinyApp(ui, server)
