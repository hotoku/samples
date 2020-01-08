library(logging)

basicConfig()
addHandler(writeToFile, file="logging/4.log")

loginfo("2")

# logファイルを指定するにはaddHandlerで
