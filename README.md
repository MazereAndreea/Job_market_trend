# 📊 Job Market Trend

_A Machine Learning project for personal use_

---

## Overview

Welcome! This repository contains my exploration of **job market trends** using data science and machine learning techniques. As part of my learning journey at University Politehnica Bucharest (Industrial Engineering & Robotics), I created this project to practice working with data, build ML models, and gain insights into the ever-evolving job market.

Docker image: https://hub.docker.com/repository/docker/andreeamaz/job_market_trend/general

---

## Data Source

- [Job Description Dataset from Kaggle](https://www.kaggle.com/datasets/ravindrasinghrana/job-description-dataset)
  - Contains detailed job descriptions, titles, and related attributes from diverse industries.
- Reddit API
  - Used to collect relevant posts and comments about jobs, industries, and career perspectives from tech and professional communities, providing real-world insights to complement the analysis.
---

## Project Goals

- Analyze and visualize job market data
- Experiment with different machine learning algorithms
- Practice working with Jupyter Notebooks and Python
- Document my process so others can learn from it too

---

## What I Did

I uploaded a comprehensive Jupyter Notebook (around 3,400 lines) where I documented every step of my analysis. Here’s a compact summary of the main actions:

### 1. Data Exploration & Cleaning
- **Loaded the dataset** and reviewed column types and missing values.
- **Analyzed missing, frequent, and unique values** using custom functions (I moved these functions into a separate file to keep the code modular)
- **Categorical encoding:** Converted categorical columns (like job title and benefits) to numerical form for ML algorithms using one-hot and multi-hot encoding
Note: The Kaggle dataset required minimal preprocessing, as it was already well-cleaned. I only performed a few minor adjustments to prepare it for feeding into ML models.

### 2. Feature Engineering
- **Extracted broader jobs and roles titles** from job descriptions using NLP techniques (feeding embeddings from sentence transformer models to KMeans model)
- **Created new columns:** For example, Salary (0 (Low), 1 (Medium), 2 (High)), Company size (0 (Small), 1 (Medium), 2 (Large)), Experience (from X to Y Years -> Average experience number), Min and Max Salary

### 3. Data Visualization
All visualizations were created in PowerBI and compiled into a dashboard report:
- **Explored distributions:** Interactive charts for job types, locations, and salary ranges.
- **Skill Analysis:** Frequency visuals for top skills required across job listings.
- **Trend Analysis:** Time-based visuals to uncover patterns in demand for roles and skills.
- **Correlation Insights:** Heatmaps and scatter plots to highlight relationships between features (skills, salary, job type, location).
- **Dashboard Report:** All findings presented in an interactive PowerBI dashboard for easy exploration.

### 4. Machine Learning Modeling
- **Built predictive models** (e.g., linear regression and random forest regression for salary estimation).
- **Evaluated model performance** using metrics like accuracy, F1-score, and RMSE, MSE.

### 5. Documentation & Explanation
- Provided detailed comments for each step, explaining the rationale behind every transformation and modeling decision.

## 🛠️ Technologies Used

- **Jupyter Notebook** (main development environment)
- **Python** (`pandas`, `scikit-learn`, `matplotlib`, `seaborn`, and NLP libraries)
- **PowerBI** (data visualization and dashboard reporting)
- **Azure Blob Storage** (cloud data management)

---

## Structure

- `notebooks/` – Step-by-step analysis, data exploration, and model building
- `data/` – Raw and processed datasets (where available)
- `README.md` – Project overview, goals, and instructions

## Why this project?

As a student interested in data science and machine learning, I wanted to tackle a real-world problem and document my learning process.

## Notes

- This project is for personal learning and experimentation.
- Feedback, suggestions, and questions are welcome!

## What's next?
- I plan to collect data directly from Reddit using their API and build a model based on real, live data.
- Implement ETL data pipeline using Apache Airflow.
- Build a deep neural network using pytorch and tensorflow
