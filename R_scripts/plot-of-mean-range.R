#This script was used based on range_dist.csv which can be generated from the range_avg_percent.sql query.

install.packages("ggplot")
library(ggplot2)
range_dist <- read.csv("range_dist.csv")

ggplot(data=range_dist, aes(x=avg_mean, y=mean_range)) +
  geom_point(color="blue",
             fill="blue",
             shape=21,
             alpha=0.5,
             size=5,
             stroke = 2)+
  theme_bw()+
  xlab("Average Mean Score")+
  ylab("Range of Score")+
#  coord_cartesian(xlim = c(1,5), ylim = c(0, 1)) +
  geom_smooth(color='grey')+
  labs(title = "Quality vs. Fluctuation", 
       subtitle="Institution's Average Mean Score vs. Range of Mean Score",
       caption = "Data Source: The Philosophical Gourmet Report")

