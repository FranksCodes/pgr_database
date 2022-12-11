setwd("/Users/Frankzi/Documents/data/pgr-visualization")
range_dist <- read.csv("range_dist.csv")
ggplot(range_dist, aes(x=mean_range)) + 
  geom_histogram(aes(y = ..density..), binwidth=.1, fill="#69b3a2")+
  geom_density(alpha=.3, fill="#FF6666") +
  theme_bw()+
  xlab("Range of Mean")+
#  stat_bin(aes(y=..count.., label=..count..), geom="text")+
#  coord_cartesian(xlim = c(0,1), ylim = c(0, 26)) +
  ylab("Density")+
  labs(title = "Mean Score Fluctuation", 
       subtitle="Histogram of Range of Overall Mean Scores",
       caption = "Data Source: The Philosophical Gourmet Report")

