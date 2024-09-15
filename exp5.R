# Install and load necessary packages
install.packages(c("ggplot2", "plotly", "tm", "wordcloud", "readr", "RColorBrewer"))
library(ggplot2)
library(plotly)
library(tm)
library(wordcloud)
library(readr)
library(RColorBrewer)

# Load the dataset
data_path <- "C:/Users/hp/Documents/datasets/HousingData.csv"  # Replace with the path to your dataset file
housing_data <- read_csv(data_path)

# Inspect the dataset
str(housing_data)
summary(housing_data)

# Create a Word Cloud (for demonstration purposes)
text_data <- colnames(housing_data)
corpus <- Corpus(VectorSource(text_data))
dtm <- DocumentTermMatrix(corpus)
m <- as.matrix(dtm)
word_freqs <- rowSums(m)
word_data <- data.frame(word = names(word_freqs), freq = word_freqs)

# Plot Word Cloud
wordcloud(words = word_data$word, freq = word_data$freq, min.freq = 1, scale = c(3,0.5), colors = brewer.pal(8, "Dark2"))

# Box and Whisker Plot
ggplot(housing_data, aes(x = factor(CHAS), y = MEDV)) +  # CHAS and MEDV are example columns
  geom_boxplot() +
  ggtitle("Boxplot of Median Value of Homes by Charles River Dummy Variable") +
  xlab("Charles River Dummy Variable") +
  ylab("Median Value of Homes")

# Violin Plot
ggplot(housing_data, aes(x = factor(CHAS), y = MEDV)) +  # CHAS and MEDV are example columns
  geom_violin(fill = "lightblue") +
  ggtitle("Violin Plot of Median Value of Homes by Charles River Dummy Variable") +
  xlab("Charles River Dummy Variable") +
  ylab("Median Value of Homes")

# Linear Regression Plot
ggplot(housing_data, aes(x = RM, y = MEDV)) +  # RM is the average number of rooms per dwelling
  geom_point() +
  geom_smooth(method = "lm", color = "blue") +
  ggtitle("Linear Regression of Median Value of Homes vs. Average Number of Rooms") +
  xlab("Average Number of Rooms") +
  ylab("Median Value of Homes")

# Nonlinear Regression Plot
ggplot(housing_data, aes(x = RM, y = MEDV)) +
  geom_point() +
  geom_smooth(method = "loess", color = "red") +
  ggtitle("Nonlinear Regression of Median Value of Homes vs. Average Number of Rooms") +
  xlab("Average Number of Rooms") +
  ylab("Median Value of Homes")

# 3D Scatter Plot
plot_ly(housing_data, x = ~RM, y = ~AGE, z = ~MEDV, type = 'scatter3d', mode = 'markers') %>%
  layout(title = "3D Scatter Plot of Median Value of Homes vs. Number of Rooms and Age of House",
         scene = list(xaxis = list(title = 'Average Number of Rooms'),
                      yaxis = list(title = 'Age of House'),
                      zaxis = list(title = 'Median Value of Homes')))

# Jitter Plot
ggplot(housing_data, aes(x = factor(CHAS), y = MEDV)) +
  geom_jitter(width = 0.2, height = 0) +
  ggtitle("Jitter Plot of Median Value of Homes by Charles River Dummy Variable") +
  xlab("Charles River Dummy Variable") +
  ylab("Median Value of Homes")
