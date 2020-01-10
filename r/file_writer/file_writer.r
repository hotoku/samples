library(R6)

file_writer <- R6Class(
  "file_writer",
  public = list(
    initialize = function(path, append=FALSE){
      private$path <- path
      if(append) return()
      if(!file.exists(path)) return()
      if(dir.exists(path)) stop(sprintf("%s is directory", path))
      file.remove(path)
    },
    write = function(lines){
      write_lines(lines, private$path, append = TRUE) 
    }      
  ),
  private = list(
    path = character(0)
  )
)

path <- "file_writer/temp.txt"
fw <- file_writer$new(path)
for(i in 1:100){
  if(i %% 15 == 0){
    fw$write("FizzBuzz")
  } else if (i %% 3 == 0){
    fw$write("Fizz")
  } else if (i %% 5 == 0){
    fw$write("Buzz")
  } else {
    fw$write(i)
  }
}

print(read_lines(path))
