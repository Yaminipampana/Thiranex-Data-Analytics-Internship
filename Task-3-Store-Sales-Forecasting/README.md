# Predictive Analytics Using Historical Data

## Project Overview

This project focuses on building a predictive analytics model using historical retail sales data. The objective is to analyze past sales trends, perform data preprocessing, and develop a machine learning model capable of forecasting future sales patterns.

The project demonstrates the complete predictive analytics workflow, including data cleaning, exploratory data analysis (EDA), feature engineering, model building, evaluation, and visualization.

---

## Objectives

* Analyze historical sales data
* Clean and preprocess large datasets
* Perform trend and pattern analysis
* Build a predictive model using Linear Regression
* Evaluate model performance
* Visualize sales trends and predictions
* Learn practical predictive analytics techniques

---

## Dataset

Dataset: Store Sales Time Series Forecasting

Files Used:

* train.csv
* stores.csv
* oil.csv
* holidays_events.csv
* transactions.csv

Dataset contains historical retail sales records from multiple stores across several years.

## Dataset

The dataset used in this project is available on Kaggle:

https://www.kaggle.com/competitions/store-sales-time-series-forecasting/data

Due to file size limitations, the dataset is not included in this repository.

---

## Technologies Used

* Python
* Pandas
* NumPy
* Matplotlib
* Seaborn
* Scikit-Learn
* Google Colab

---

## Project Workflow

### 1. Data Collection

Loaded historical sales data and supporting datasets including store information, oil prices, and holiday events.

### 2. Data Cleaning

* Checked missing values
* Removed duplicate records
* Converted date columns into datetime format

### 3. Feature Engineering

Created new features from date information:

* Year
* Month
* Day
* Day of Week
* Holiday Indicator

Encoded categorical variables for machine learning.

### 4. Exploratory Data Analysis

Performed:

* Daily Sales Trend Analysis
* Monthly Sales Analysis
* Product Family Analysis
* Correlation Analysis

### 5. Predictive Modeling

Model Used:

* Linear Regression

The model was trained to predict sales using historical sales-related features.

### 6. Model Evaluation

Performance Metrics:

* Mean Absolute Error (MAE)
* Root Mean Squared Error (RMSE)
* R² Score

### 7. Visualization

Generated visualizations including:

* Daily Sales Trend
* Monthly Sales Analysis
* Actual vs Predicted Sales
* Feature Importance

---

## Results

The predictive model successfully identified sales patterns and generated future sales predictions based on historical data.

Key findings:

* Sales showed an overall increasing trend over time.
* Promotions significantly influenced sales.
* Seasonal patterns were observed across months.
* Holidays contributed to fluctuations in sales performance.

---

## Project Structure

```text
store-sales-predictive-analytics/

│
├── data/
│   ├── train.csv
│   ├── stores.csv
│   ├── oil.csv
│   ├── holidays_events.csv
│   └── transactions.csv
│
├── notebooks/
│   └── Predictive_Analytics_Using_Historical_Data.ipynb
│
├── images/
│   ├── daily_sales_trend.png
│   ├── monthly_sales.png
│   ├── actual_vs_predicted.png
│   └── feature_importance.png
│
└── README.md
```

---

## Skills Demonstrated

* Data Cleaning
* Data Preprocessing
* Feature Engineering
* Exploratory Data Analysis
* Data Visualization
* Predictive Analytics
* Machine Learning
* Regression Modeling
* Model Evaluation

---

## Conclusion

This project demonstrates the practical implementation of predictive analytics using historical sales data. Through data preprocessing, trend analysis, machine learning, and visualization, valuable insights were generated to support data-driven decision-making and future sales forecasting.
