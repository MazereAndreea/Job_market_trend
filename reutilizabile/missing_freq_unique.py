import io
from azure.storage.blob import BlobServiceClient
from reutilizabile.common_imports import np,pd

def missing_data(data):
    total = data.isnull().sum()
    percent = (total/data.isnull().count()*100)
    tt = pd.concat([total,percent], axis=1, keys=['Total','Percent'])
    types = []
    for col in data.columns:
        dtype = str(data[col].dtype)
        types.append(dtype)
    tt['Types'] = types
    return(np.transpose(tt))

def most_frequent_values(data):
    total = data.count()
    tt = pd.DataFrame(total)
    tt.columns = ['Total']
    items = []
    vals = []
    for col in data.columns:
        try:
            itm = data[col].value_counts().index[0]
            val = data[col].value_counts().values[0]
            items.append(itm)
            vals.append(val)
        except Exception as ex:
            print(ex)
            items.append(0)
            vals.append(0)
            continue
    tt['Most frequent item'] = items
    tt['Frequence'] = vals
    tt['Percent from total'] = np.round(vals / total * 100, 3)
    return(np.transpose(tt))

def unique_values(data):
    total = data.count()
    tt = pd.DataFrame(total)
    tt.columns = ['Total']
    uniques = []
    unique_vals = {}
    for col in data.columns:
        unique = data[col].nunique()
        uniques.append(unique)
        unique_vals[col] = data[col].unique()
    tt['Uniques'] = uniques
    return(np.transpose(tt))

def save_changes(data, container_name, blob_name, connection_string):
    # Convert DataFrame to CSV in-memory
    csv_buffer = io.StringIO()
    data.to_csv(csv_buffer, index=False)
    csv_buffer.seek(0)  # Go back to start of buffer

    # Connect
    blob_service_client = BlobServiceClient.from_connection_string(connection_string)
    blob_client = blob_service_client.get_blob_client(container=container_name, blob=blob_name)

    # Upload CSV from buffer
    blob_client.upload_blob(csv_buffer.getvalue(), overwrite=True)
    print(f"File uploaded to Azure Blob Storage as {blob_name} in container {container_name}")

    return data #for further processing