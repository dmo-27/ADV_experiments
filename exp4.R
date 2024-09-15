library(ggplot2)
ggplot(USArrests, aes(x = reorder(row.names(USArrests), -Murder), y = Murder)) + 
  geom_bar(stat = "identity", fill = "skyblue") +
  coord_flip() +
  labs(title = "Murder Rates by State", x = "States", y = "Murder Rate")
