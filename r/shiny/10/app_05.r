## https://rstudio.github.io/promises/articles/casestudy.html
## を読むと、特別なことは特にしてないように見える
## ページを複数のパーツに分割したら、パーツごとに描画されるのではないかと予想
## 答え：確かに、パーツごとに描画されるが、下のコードでtextOutputが描画されるのは10秒後


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

  output$plot <- renderPlot({
    dat() %...>% (function(d)plot(x=d$x, y=d$y))
  })
}

shinyApp(ui, server)
