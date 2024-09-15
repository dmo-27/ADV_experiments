library(ggplot2)
ggplot(USArrests, aes(x = reorder(row.names(USArrests), -Murder), y = Murder)) + 
  geom_bar(stat = "identity", fill = "skyblue") +
  coord_flip() +
  labs(title = "Murder Rates by State", x = "States", y = "Murder Rate")

crime_data <- colSums(USArrests)
pie(crime_data, labels = names(crime_data), main = "Crime Distribution in USArrests Dataset")


ggplot(USArrests, aes(x = Assault)) +
  geom_histogram(binwidth = 10, fill = "lightgreen", color = "black") +
  labs(title = "Distribution of Assault Cases", x = "Number of Assaults", y = "Frequency")

ggplot(USArrests, aes(x = Assault, y = Murder)) +
  geom_point(color = "darkred") +
  labs(title = "Assault vs Murder", x = "Assault Cases", y = "Murder Cases")

ggplot(USArrests, aes(x = Murder, y = Assault, size = UrbanPop, color = UrbanPop)) +
  geom_point(alpha = 0.7) +
  labs(title = "Bubble Plot of Crime Data", x = "Murder Rate", y = "Assault Cases", size = "Urban Population (%)")

library(ggplot2)

#timeline plot

# Add a time component to USArrests dataset
USArrests$Time <- seq_len(nrow(USArrests))

# Check if Time column was added successfully
head(USArrests)


ggplot(USArrests, aes(x = Time, y = Murder)) +
  geom_line(color = "blue", size = 1) +
  geom_point(color = "red", size = 3) +
  labs(title = "Murder Rates Over Time (Simulated)", x = "Time (Arbitrary)", y = "Murder Rate") +
  theme_minimal()
