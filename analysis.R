data <- read.csv("whois.csv")

na_count <-sapply(data, function(y) sum(length(which(is.na(y)))))
na_count

is.null(data)

data <- data[, -which(colMeans(is.na(data)) > 0.5)]
data <- data[, -which(colMeans(as.data.frame(as.matrix(data)=="")) > 0.5)]

cols <- names(data)[!names(data)%in%c("creation_date", "expiration_date")]

data[cols] <- lapply(data[cols], as.factor)

summary(subset(data, select = -url))