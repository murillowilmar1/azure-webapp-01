import requests
from azure.storage.blob import BlobServiceClient
from datetime import datetime

# Reemplaza con la cadena de conexión completa de tu cuenta de almacenamiento


# URL del archivo público
file_url = 'https://www.w3.org/WAI/ER/tests/xhtml/testfiles/resources/pdf/dummy.pdf'

# Descargar el archivo
response = requests.get(file_url)
if response.status_code == 200:
    file_name = file_url.split("/")[-1]  # Nombre original del archivo
    timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
    unique_file_name = f"{timestamp}_{file_name}"

    # Conectar a Blob Storage
    blob_service_client = BlobServiceClient.from_connection_string(STORAGE_CONNECTION_STRING)
    blob_client = blob_service_client.get_blob_client(container=CONTAINER_NAME, blob=unique_file_name)
    
    # Subir el contenido del archivo descargado
    blob_client.upload_blob(response.content)
    print(f"Archivo descargado y almacenado como {unique_file_name} en Blob Storage.")
else:
    print(f"Error al descargar el archivo. Código de estado: {response.status_code}")
