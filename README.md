# 📊 Job Market Trend

_A Machine Learning project for personal use_

---

## Overview

Welcome! This repository contains my exploration of **job market trends** using data science and machine learning techniques. As part of my learning journey at University Politehnica Bucharest (Industrial Engineering & Robotics), I created this project to practice working with data, build ML models, and gain insights into the ever-evolving job market.

---

## Data Source

- [Job Description Dataset from Kaggle](https://www.kaggle.com/datasets/ravindrasinghrana/job-description-dataset)
  - Contains detailed job descriptions, titles, and related attributes from diverse industries.

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
- **Handled missing data:** Identified columns with nulls and chose appropriate strategies (drop, fill, or ignore) for each.
- **Standardized text fields:** Cleaned job titles, descriptions, and company names (lowercasing, removing punctuation, etc.).
- **Categorical encoding:** Converted categorical columns (like job type and location) to numerical form for ML algorithms.

### 2. Feature Engineering
- **Extracted skills and keywords** from job descriptions using NLP techniques.
- **Created new columns:** For example, skills count, keyword presence, job seniority level (based on title), and location clustering.
- **Transformed date/time fields** to derive insights on job posting trends.

### 3. Data Visualization
All visualizations were created in PowerBI and compiled into a dashboard report:
- **Explored distributions:** Interactive charts for job types, locations, and salary ranges.
- **Skill Analysis:** Frequency visuals for top skills required across job listings.
- **Trend Analysis:** Time-based visuals to uncover patterns in demand for roles and skills.
- **Correlation Insights:** Heatmaps and scatter plots to highlight relationships between features (skills, salary, job type, location).
- **Dashboard Report:** All findings presented in an interactive PowerBI dashboard for easy exploration.

### 4. Machine Learning Modeling
- **Built predictive models** (e.g., classification to predict job category, regression for salary estimation).
- **Evaluated model performance** using metrics like accuracy, F1-score, and RMSE.
- **Used cross-validation** and hyperparameter tuning for better results.

### 5. Documentation & Explanation
- Provided detailed comments for each step, explaining the rationale behind every transformation and modeling decision.

## 🛠️ Technologies Used

- **Jupyter Notebook** (main development environment)
- **Python** (`pandas`, `numpy`, `scikit-learn`, `matplotlib`, `seaborn`, and NLP libraries)
- **PowerBI** (data visualization and dashboard reporting)
- **Oracle Autonomous Database & Object Storage** (cloud data management)

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
