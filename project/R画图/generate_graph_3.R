# Load data
data <- read.csv("weibo_friends_counts.csv", sep=",", header=TRUE)

# filter
data <- data[data$Average.Count<500,]
data <- data[data$Fans.Count<500,]

# Density plot

fans <- density(data$Fans.Count[!is.na(data$Fans.Count)])
average <- density(data$Average.Count[!is.na(data$Average.Count)])

#暂时没有搞懂polygon的工作原理，这部分以后再解决。
#x <- (c(fans$x,average$x))
#y <- c(fans$y,average$y)
#plot(x,y,type="n")
#polygon(x,y, border=c("blue","red"))

#将多个密度图画在一张图上的权宜之计
plot(average,col="red",xlab="粉丝数量", ylab="密度", main="密度图对比")
#polygon(average)
lines(fans, col="blue")