# プロットに日本語を入れる方法
# 参考：https://stackoverflow.com/questions/31859911/r-shiny-server-not-rendering-correct-ggplot-font-family


library(shiny)
library(tidyverse)

makePlot <- function(dat, x, y, width, height, pixelratio, ...){
  outfile <- tempfile(fileext='.png')
  
  png(outfile, width=width*pixelratio, height=height*pixelratio,
      res=72*pixelratio)
  p <- dat %>%
    ggplot(aes_string(x, y)) +
    geom_point()
  print(p)
  dev.off()
  
  list(src = outfile,
       width = width,
       height = height,
       alt = "This is alternate text")
}

dat <- tibble(
  エックス=1:10,
  ワイ=1:10
)


ui <- fluidPage(
  imageOutput("image")
)

server <- function(input, output, session){
  output$image <- renderImage({
    imageName <- "image" # imageOutputのoutputId
    width  <- session$clientData[[sprintf("output_%s_width", imageName)]]
    height <- session$clientData[[sprintf("output_%s_height", imageName)]]
    pixelratio <- session$clientData$pixelratio

    makePlot(dat, "エックス", "ワイ", width, height, pixelratio)
  }, deleteFile = TRUE)
}

shinyApp(ui, server)
