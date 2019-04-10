library(jsonlite)
install.packages("readr") # you only need to do this one time on your system

library(readr)
mystring <- read_file("whois.json")


j <- fromJSON(mystring, flatten = T)
j


#d = {"col1":[1, 3], "col2":[4, 2]}


d = {'one': [1., 2., 3., 4.],
     'two': [4., 3., 2., 1.]}