import sys
import os
from reutilizabile.common_imports import *
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))
from reutilizabile.blob import load_blob_csv_to_df
from reutilizabile.plots import *
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, confusion_matrix, ConfusionMatrixDisplay, classification_report
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder, StandardScaler
import streamlit as st
import streamlit.components.v1 as components
from azure.storage.blob import BlobServiceClient
from dotenv import load_dotenv
import joblib
load_dotenv()
st.set_page_config(layout="wide")

connection_string = os.getenv("AZURE_STORAGE_CONNECTION_STRING")
container = os.getenv("AZURE_STORAGE_CONTAINER", "jobs")
blob_name = os.getenv("AZURE_STORAGE_BLOB", "job_description.csv")

# Decorator to cache functions that return data
@st.cache_data
def get_data():
	return load_blob_csv_to_df(connection_string, container, blob_name)

try:
	df = get_data()
	st.success("Load successfully")
	st.dataframe(df.head(50))
except Exception as e:
	st.error(f"Didn't load successfully because {e}")

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


model2 = joblib.load('model2.pkl')
y_pred2 = model2.predict(X_test) #random forest model

st.header("Model Evaluation Metrics")
accuracy = accuracy_score(y_test, y_pred2)
precision = precision_score(y_test, y_pred2, average='weighted')
recall = recall_score(y_test, y_pred2, average='weighted')
f1 = f1_score(y_test, y_pred2, average='weighted')
cm = confusion_matrix(y_test, y_pred2)
st.metric("Accuracy", accuracy)
st.metric("Precision", precision)
st.metric("Recall", recall)
st.metric("F1 Score", f1)
disp = ConfusionMatrixDisplay(confusion_matrix=cm)
disp.plot()








