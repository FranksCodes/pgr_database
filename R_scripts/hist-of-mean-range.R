#This was used to generate the histogram based on range_dist.csv, generated from range_avg_percent.sql. 

range_dist <- read.csv("range_dist.csv")
ggplot(range_dist, aes(x=mean_range)) + 
  geom_histogram(aes(y = ..density..), binwidth=.1, fill="#69b3a2")+
  geom_density(alpha=.3, fill="#FF6666") +
  theme_bw()+
  xlab("Range of Mean")+
  ylab("Density")+
  labs(title = "Mean Score Fluctuation", 
       subtitle="Histogram of Range of Overall Mean Scores",
       caption = "Data Source: The Philosophical Gourmet Report")

