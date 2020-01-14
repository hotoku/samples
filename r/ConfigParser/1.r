library(ConfigParser)

conf <- ConfigParser$new()$read("ConfigParser/1.conf")
print(conf$get("json"))
