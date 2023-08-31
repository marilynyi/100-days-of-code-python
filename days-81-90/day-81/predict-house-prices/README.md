# Day 81: Predicting House Prices

Imagine you're working for a real estate development company in Boston, Massachusetts in the 1970s. Your company wants to value any residential project before they start. You are tasked with building a model that can provide a price estimate based on a home's characteristics like:
- The number of rooms
- The distance to employment centers
- How rich or poor the area is
- How many students there are per teacher in local schools, etc.
  
Learning objectives:
- Quickly spot relationships in a dataset using Seaborn's `.pairplot()`
- Split the data into a training and testing dataset to better evaluate a model's performance
- Run a multivariable regression
- Evaluate that regression based on the sign of its coefficients
- Analyze and look for patterns in a model's residuals
- Improve a regression model using (a log) data transformation
- Specify your own values for various features and use your model to make a prediction