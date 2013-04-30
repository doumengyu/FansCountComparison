data <- read.csv("weibo_friends_counts.csv", sep=",", header=TRUE)

# filter
data <- data[data$Fans.Count>200,]
data <- data[data$Fans.Count<420,]

counts <- data.frame(data$Weibo.ID,data$Fans.Count,data$Average.Count)
mymat <- t(counts[-1])
colnames(mymat) <- counts[, 1]
barplot(mymat, beside = TRUE,xlab="Weibo Users", col=c("darkblue","red"),main="新浪微博用户粉丝数与好友粉丝数平均值比较",
	cex.names = 0.5,legend = c("用户粉丝数","用户好友粉丝数平均值"))
