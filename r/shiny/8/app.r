# 環境変数を列挙してみる

library(shiny)

ui <- fluidPage(
  tableOutput("table")
)

server <- function(input, output, session){
  output$table <- renderTable({
    env <- Sys.getenv()
    nm <- names(env)
    vl <- sapply(nm, function(n)env[[n]])
    data.frame(name=nm, value=vl)
  })
}

shinyApp(ui, server)
