#Gold Price Prediction Using Linear Regression

This project provides a predictive analysis of gold prices based on the EUR/USD exchange rate using Linear Regression. Leveraging a dataset with various financial indicators, the project seeks to establish the relationship between currency exchange rates and commodity prices, specifically gold.

#Table of Contents

Introduction
Dataset Description
Project Workflow
Features and Target Variable
Model Evaluation
Conclusion
License

#Introduction

The Gold Price Prediction project is designed to help users predict gold prices by analyzing fluctuations in the EUR/USD exchange rate. This project can be valuable for financial analysts, data scientists, and anyone interested in the interplay between currency exchange rates and commodity values.

#Dataset Description

The dataset, gld_price_data.csv, contains records of daily gold prices along with financial indicators that provide context on global economic conditions. It is structured with the following columns:

Date: Date of the record
SPX: S&P 500 index value
GLD: Gold price per ounce in USD (target variable)
USO: United States Oil Fund price, an indicator of oil prices
SLV: Price of silver per ounce
EUR/USD: Daily exchange rate between the Euro and U.S. Dollar
Project Workflow
This project follows a systematic approach:

#Data Loading:

Loading and initial inspection of the dataset to understand its structure.

#Data Splitting:

Splitting the data into training and testing sets to evaluate the model’s performance.

#Modeling:

Applying Linear Regression to predict GLD (gold prices) based on EUR/USD (exchange rates).

#Prediction and Visualization:

Visualizing the model’s predictions on both training and testing data for insights into performance.

#Evaluation:

Calculating performance metrics to gauge the accuracy of predictions.

#Features and Target Variable

#Feature

EUR/USD: The exchange rate between the Euro and U.S. Dollar, used as the independent variable for predicting gold prices.

#Target Variable

GLD: The price of gold per ounce in USD, used as the dependent variable.

#Model Evaluation
The model’s performance is assessed using the following metrics:

R² Score: Measures the proportion of variance in gold prices explained by the EUR/USD rate.
Mean Absolute Error (MAE): Represents the average absolute error between predicted and actual values.
Mean Squared Error (MSE): Calculates the average of squared differences between predictions and actual values.
Median Absolute Error (MedAE): Indicates the median of absolute errors, less affected by outliers.
Explained Variance Score (EVS): Indicates the proportion of variance explained by the model.

#Conclusion

The Gold Price Prediction project highlights how currency exchange rates can impact gold prices, providing insights into the relationship between global financial indicators and commodity markets. This project serves as a foundational model for further analysis in financial forecasting and trend prediction.
