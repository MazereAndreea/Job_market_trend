import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))
from reutilizabile.common_imports import *
from reutilizabile.blob import load_blob_csv_to_df
from reutilizabile.plots import *
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, confusion_matrix, ConfusionMatrixDisplay, classification_report
from sklearn.preprocessing import OneHotEncoder, StandardScaler
import streamlit as st
import streamlit.components.v1 as components
from azure.storage.blob import BlobServiceClient
from matplotlib.ticker import MultipleLocator
import toml
import joblib
st.set_page_config(layout="wide")

# connection_string = st.secrets["AZURE_STORAGE_CONNECTION_STRING"]
# container = st.secrets.get("AZURE_STORAGE_CONTAINER", "jobs")
# blob_name = st.secrets.get("AZURE_STORAGE_BLOB", "job_description.csv")
connection = st.secrets["AZURE_STORAGE_BLOB_URL"]

# Decorator to cache functions that return data
# @st.cache_data
# def get_data():
# 	return load_blob_csv_to_df(connection_string, container, blob_name)

# try:
# 	df = get_data()
# 	st.success("Load successfully")
# 	st.dataframe(df.head())
# except Exception as e:
# 	st.error(f"Didn't load successfully because {e}")

df = pd.read_csv(connection)
target_column = "Salary_Tercile" #the desired prediction
feature_columns = [
    "Qualifications",
    "Average_experience",
    "Work Type",
    "Company size",
    "Job Area",
    "Role cluster",
    "Bonuses and Incentive Programs",
    "Casual Dress Code",
    "Childcare Assistance",
    "Employee Assistance Programs (EAP)",
    "Employee Discounts",
    "Employee Recognition Programs",
    "Employee Referral Programs",
    "Financial Counseling",
    "Flexible Spending Accounts (FSAs)",
    "Flexible Work Arrangements",
    "Health Insurance",
    "Health and Wellness Facilities",
    "Legal Assistance",
    "Life and Disability Insurance",
    "Paid Time Off (PTO)",
    "Parental Leave",
    "Professional Development",
    "Profit-Sharing",
    "Relocation Assistance",
    "Retirement Plans",
    "Social and Recreational Activities",
    "Stock Options or Equity Grants",
    "Transportation Benefits",
    "Tuition Reimbursement",
    "Wellness Programs"
] #features taken into account for the model

# Assign X,Y with features and target

X = df[feature_columns]
Y = df[target_column]

# Split the dataset for training 80% and testing 20%
X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size=0.2, random_state=42)

# Load the trained model
model1 = joblib.load('model1.pkl')
y_pred1 = model1.predict(X_test) #logistic regression model

st.header("Model Evaluation Metrics")
accuracy = accuracy_score(y_test, y_pred1)
precision = precision_score(y_test, y_pred1, average='weighted')
recall = recall_score(y_test, y_pred1, average='weighted')
f1 = f1_score(y_test, y_pred1, average='weighted')
cm = confusion_matrix(y_test, y_pred1)
print(f"Accuracy: {accuracy}, Precision: {precision}, Recall: {recall}, f1 score: {f1}")
disp = ConfusionMatrixDisplay(confusion_matrix=cm)
disp.plot()
st.metric("Accuracy", accuracy)
st.metric("Precision", precision)
st.metric("Recall", recall)
st.metric("F1 Score", f1)

#Conclusion: standard deviation is low, so linear regression doesn't work well, i'm using logistic regression instead and make classes of salary






