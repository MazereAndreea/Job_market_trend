import os
from azure.storage.blob import BlobServiceClient
import pandas as pd
from dotenv import load_dotenv
from io import StringIO
load_dotenv()

def load_blob_csv_to_df(
    connection_string: str,
    container_name: str,
    blob_name: str
) -> pd.DataFrame:
    """
    Downloads a CSV blob from Azure Blob Storage and returns it as a pandas DataFrame.
    """
    # Initialize BlobServiceClient
    blob_service_client = BlobServiceClient.from_connection_string(connection_string)

    # Get blob client
    blob_client = blob_service_client.get_blob_client(container=container_name, blob=blob_name)

    # Download blob content
    stream_downloader = blob_client.download_blob()
    blob_bytes = stream_downloader.readall()

    # Convert bytes to string and read as DataFrame
    blob_str = blob_bytes.decode('utf-8')
    df = pd.read_csv(StringIO(blob_str))

    return df

# Optional: example usage for debugging (won't run on import)
if __name__ == "__main__":
    connection_string = os.getenv("AZURE_STORAGE_CONNECTION_STRING")
    container = os.getenv("AZURE_STORAGE_CONTAINER", "jobs")
    blob_name = os.getenv("AZURE_STORAGE_BLOB", "job_description.csv")
    df = load_blob_csv_to_df(connection_string, container, blob_name)
    print(df.head())
