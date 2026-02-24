# 🎬 IMDb Movie Data Analysis
Exploratory Data Analysis (EDA) and Business Intelligence using Python.

---

## 📌 1. Project Overview

This project performs Exploratory Data Analysis (EDA) on a cleaned IMDb movie dataset.  
The objective is to analyze movie ratings, financial performance, audience engagement, and industry trends using Python.

---

## 📂 2. Dataset Information

**Dataset Name:** cleaned_IMDB_dataset.csv  

### Columns Included:
- imdb_id
- title
- release_date
- genre
- duration
- country
- content_rating
- director
- income
- votes
- score

---

## 🧹 3. Data Cleaning & Preparation

The following preprocessing steps were performed:

- Converted `release_date` to datetime format
- Extracted `release_year`
- Converted `duration`, `income`, `votes`, and `score` to numeric
- Replaced infinite values with NaN
- Handled missing values
- Removed unrealistic duration values

### Data Quality Checks:
- Checked dataset shape
- Verified column data types
- Identified missing values
- Cleaned infinite values

---

## 📊 4. Exploratory Data Analysis

### 🎯 4.1 IMDb Score Distribution
- Most movies fall between 6–8 rating range
- Very few movies have extremely high ratings

### 🎯 4.2 Movie Duration Analysis
- Majority of movies range between 90–150 minutes
- Outliers were removed for better visualization

### 🎯 4.3 Release Trend Analysis
- Movie production increased significantly after 2000
- Recent years show steady growth

---

## 📈 5. Relationship Analysis

### 💰 Income vs IMDb Score
- Weak to moderate correlation observed
- High revenue does not always guarantee high ratings

### ⭐ Votes vs Score
- Movies with higher votes tend to have slightly higher ratings
- Audience engagement impacts visibility

---

## 🏆 6. Categorical Insights

### 🎬 Top Genres
- Drama and Action are dominant genres
- Some genres consistently perform better in ratings

### 🌍 Top Producing Countries
- Few countries dominate movie production
- Geographic concentration observed

---

## 🔥 7. Correlation Analysis

A correlation heatmap revealed:

- Strong correlation between `votes` and `income`
- Moderate relationship between `votes` and `score`
- Weak correlation between `duration` and `score`

---

## 🏅 8. Top 10 Highest Rated Movies

Movies were sorted by `score` to identify top performers.

Insights:
- High-rated movies often have high vote counts
- Critical success and financial success do not always align

---

## 📊 9. Visualization Techniques Used

- Histogram
- Line Plot
- Scatter Plot
- Bar Chart
- Pie Chart
- Box Plot
- Pair Plot
- Heatmap

---

## 🛠 Tools & Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Jupyter Notebook

---

## 🚀 Conclusion

This EDA provides insights into movie performance trends, audience engagement, and financial outcomes.  
The analysis highlights that audience interaction plays a crucial role in movie popularity, while financial success and ratings do not always correlate directly.

---

### 📌 Author
IMDb Data Analysis Project  
