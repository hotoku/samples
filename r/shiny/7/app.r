# 環境変数が読めるかの確認
# ダメだったぽい・・

library(shiny)

ui <- fluidPage(
  textOutput("text")
)

server <- function(input, output, session){
  output$text <- renderText({
    if(Sys.getenv("HOTOKU_SHINYSERVER") == "1"){
      "environment variable is set"
    } else {
      "environment variable is not set"
    }
  })
}

shinyApp(ui, server)
