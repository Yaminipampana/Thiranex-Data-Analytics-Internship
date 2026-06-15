# Customer Segmentation and Customer Insights Dashboard

## Overview

This project focuses on customer segmentation using Machine Learning and Business Intelligence techniques. Customers are grouped into meaningful segments based on their Annual Income and Spending Score using the K-Means Clustering algorithm. The segmented data is then visualized through an interactive Power BI dashboard to generate business insights and support data-driven decision-making.

## Project Objectives

* Analyze customer behavior and purchasing patterns.
* Segment customers into distinct groups using K-Means Clustering.
* Visualize customer segments through an interactive Power BI dashboard.
* Generate actionable customer insights and marketing recommendations.
* Support business decision-making using customer analytics.

## Technologies Used

### Programming & Analytics

* Python
* Pandas
* NumPy
* Scikit-Learn
* Matplotlib

### Business Intelligence

* Power BI
* DAX

## Dataset

The project uses the Mall Customers Dataset containing:

| Feature                | Description                           |
| ---------------------- | ------------------------------------- |
| CustomerID             | Unique customer identifier            |
| Genre                  | Customer gender                       |
| Age                    | Customer age                          |
| Annual Income (k$)     | Annual income in thousands of dollars |
| Spending Score (1-100) | Customer spending behavior score      |

## Methodology

### 1. Data Collection

* Imported customer dataset.
* Selected relevant features for segmentation.

### 2. Data Preprocessing

* Loaded and analyzed dataset.
* Checked data quality.
* Selected Annual Income and Spending Score as clustering features.

### 3. Elbow Method

* Applied the Elbow Method to determine the optimal number of clusters.
* Identified K = 5 as the optimal number of customer segments.

### 4. K-Means Clustering

* Trained K-Means clustering model.
* Assigned each customer to a cluster.
* Generated customer segment labels.

### 5. Dashboard Development

* Exported segmented dataset.
* Built an interactive Power BI dashboard.
* Added KPI cards, charts, filters, and customer insights.

## Customer Segments Identified

### High Income – High Spending

* Most valuable customers.
* Ideal for premium products and loyalty programs.

### High Income – Low Spending

* High purchasing power but low engagement.
* Opportunity for targeted marketing campaigns.

### Low Income – High Spending

* Active buyers who respond well to discounts and promotions.

### Low Income – Low Spending

* Lowest engagement customer segment.

### Average Customers

* Largest customer base with moderate purchasing behavior.

## Dashboard Features

### KPI Cards

* Total Customers
* Average Income
* Average Spending Score
* Total Customer Segments

### Visualizations

* Customer Distribution by Segment
* Gender Distribution Analysis
* Average Income by Segment
* Average Spending by Segment
* Customer Segmentation Scatter Plot

### Interactive Features

* Segment Filter
* Dynamic Visual Analysis
* Business Insights

## Key Insights

* High Income High Spending customers represent the most profitable segment.
* Average Customers form the largest customer group.
* High Income Low Spending customers present significant growth opportunities.
* Low Income High Spending customers are highly responsive to promotional offers.
* Customer segmentation enables targeted marketing strategies and improved customer retention.

## Results

* Successfully segmented customers into 5 meaningful groups.
* Developed an interactive Power BI dashboard.
* Generated customer insights for business decision-making.
* Demonstrated practical application of Machine Learning and Business Intelligence.

## Project Structure

```text
Customer-Segmentation-Dashboard/
│
├── customer_segmentation.py
├── Mall_Customers.csv
├── Customer_Segments_Output.csv
├── Customer Segmentation Dashboard.pbix
├── README.md
└── screenshots
```

## Future Enhancements

* Real-time customer segmentation.
* Integration with SQL databases.
* Predictive customer behavior analysis.
* Customer Lifetime Value (CLV) prediction.
* Deployment using Power BI Service.
