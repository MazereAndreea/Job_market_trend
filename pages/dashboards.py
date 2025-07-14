import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))
from reutilizabile.blob import load_blob_csv_to_df
import streamlit as st
import streamlit.components.v1 as components
from azure.storage.blob import BlobServiceClient
from dotenv import load_dotenv
load_dotenv()

connection_string = os.getenv("AZURE_STORAGE_CONNECTION_STRING")
container = os.getenv("AZURE_STORAGE_CONTAINER", "jobs")
blob_name = os.getenv("AZURE_STORAGE_BLOB", "job_description.csv")

def get_data():
	return load_blob_csv_to_df(connection_string, container, blob_name)

st.title("Power BI Report")

try:
	df = get_data()
	st.success("Load successfully")
	st.dataframe(df.head(50))
except Exception as e:
	st.error(f"Didn't load successfully because {e}")


