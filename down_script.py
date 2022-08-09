from io import BytesIO
from azure.storage.blob import BlobServiceClient, BlobClient, ContainerClient, __version__
import pandas as pd

# Get the connection string from Shared Access Signature
connect_str = "BlobEndpoint=https://bdacademy.blob.core.windows.net/?sv=2021-06-08&ss=bfqt&srt=sco&sp=rwdlacupiytfx&se=2022-08-09T15:31:45Z&st=2022-08-09T07:31:45Z&spr=https&sig=gM31xrn3%2BBBGcc%2BzO%2FGiRjsSgetawWItuzkzssJWB6g%3D"
container_name = "datasources"
blob_name = "salary.csv"
blob_name2 = "savings.csv"

blob_service_client = BlobServiceClient.from_connection_string(connect_str)
blob_client = blob_service_client.get_blob_client(container=container_name, blob=blob_name)
blob_client2 = blob_service_client.get_blob_client(container=container_name, blob=blob_name2)

df1 = pd.DataFrame()
df2 = pd.DataFrame()

with BytesIO() as input_blob:
    blob_client.download_blob().download_to_stream(input_blob)
    input_blob.seek(0)
    df = pd.read_csv(input_blob, sep=";")
    print(df.to_string())
    df.to_csv("downloaded_salary.csv")

with BytesIO() as input_blob:
    blob_client2.download_blob().download_to_stream(input_blob)
    input_blob.seek(0)
    df = pd.read_csv(input_blob, sep=";")
    print(df.to_string())
    df.to_csv("downloaded_savings.csv")
#df3=pd.merge(df1,df2, on='id')

