## 単純にデータをdlして表示するパターン。
## この場合は、クライアントが待たされる。 
## アクセス直後は何も描画されず、３秒後にtextも含めて同時に描画される。 

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
    dat <- downLoadData()
    plot(dat$x, dat$y)
  })
}

shinyApp(ui, server)
