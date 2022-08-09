# https://portal.azure.com/#@datasentics.onmicrosoft.com/resource/subscriptions/3e4ab56a-21ee-4c7f-b438-6f831990ff7f/resourceGroups/adap-cz-demo-rg-dev/providers/Microsoft.Storage/storageAccounts/mikulasdemo/overview

import os, uuid
from azure.storage.blob import BlobServiceClient, BlobClient, ContainerClient, __version__

# Get the connection string from Shared Access Signature
# connect_str = "https://mikulasdemo.blob.core.windows.net/;QueueEndpoint=https://mikulasdemo.queue.core.windows.net/;FileEndpoint=https://mikulasdemo.file.core.windows.net/;TableEndpoint=https://mikulasdemo.table.core.windows.net/;SharedAccessSignature=sv=2021-06-08&ss=bfqt&srt=sco&sp=rwdlacupiytfx&se=2022-08-31T15:05:23Z&st=2022-08-06T07:05:23Z&spr=https,http&sig=C03vlTaI6wp7rVDqS56FYmdD2Lp2W4%2BoC2CXdFYerJo%3D"
connect_str3 = "BlobEndpoint=https://bdacademy.blob.core.windows.net/?sv=2021-06-08&ss=bfqt&srt=sco&sp=rwdlacupiytfx&se=2022-08-31T15:33:52Z&st=2022-08-09T07:33:52Z&spr=https&sig=66NHfW%2FPPySH9IfpsX0pMj%2Fymjdh2xJVPFf3o9Rw4vA%3D"
container_name2 = "EdiO"
local_file_name = "./downloaded_salary.csv"
local_file_name1 = "./downloaded_savings.csv"

blob_service_client = BlobServiceClient.from_connection_string(connect_str3)

blob_client = blob_service_client.get_blob_client(container=container_name2, blob=local_file_name)

with open(local_file_name, "rb") as file:
	blob_client.upload_blob(file)

blob_client1 = blob_service_client.get_blob_client(container=container_name2, blob=local_file_name1)

with open(local_file_name1, "rb") as file:
	blob_client1.upload_blob(file)

