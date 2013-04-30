data <- read.csv("weibo_friends_counts.csv", sep=",", header=TRUE)

# filter
data <- data[data$Average.Count<500,]
data <- data[data$Fans.Count<500,]

breaks = seq(0, 500, by=50)

par(mfrow=c(2,1))
hist(data$Fans.Count, breaks=breaks, ylim = c(0,15),xlab="用户的粉丝数",main="用户粉丝数分布直方图",horiz=TRUE,col="blue")
hist(data$Average.Count, breaks=breaks, ylim = c(0,15),xlab="用户好友的平均粉丝数",main="用户好友平均粉丝数分布直方图",horiz=TRUE,col="red")