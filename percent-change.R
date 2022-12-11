install.packages("ggplot")
library(ggplot2)
setwd("/Users/Frankzi/Documents/data/pgr-visualization")
change_dist <- read.csv("percent_change.csv")

ggplot(data=change_dist, aes(x=avg_mean, y=percent_change)) +
  geom_point(color="blue",
             fill="purple",
             shape=21,
             alpha=0.5,
             size=5,
             stroke = 2)+
  theme_bw()+
  xlab("Average Mean Score")+
  ylab("Percent Change")+
  geom_smooth(color='grey')+
  labs(title = "Quality vs. Fluctuation", 
       subtitle="Institution's Average Mean score vs. Percent Fluctuation",
       caption = "Data Source: The Philosophical Gourmet Report")

