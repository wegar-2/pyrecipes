import json
import google.auth
from google.auth.transport.requests import Request
from google.oauth2 import service_account
import requests

from mysecrets.mysecrets import endpoint_url, sa_json_path

# Path to your service account key file
SERVICE_ACCOUNT_FILE = str(sa_json_path)

# The URL of your Cloud Run service
CLOUD_RUN_URL = endpoint_url

# Load the service account credentials
credentials = service_account.Credentials.from_service_account_file(
    SERVICE_ACCOUNT_FILE,
    scopes=['https://www.googleapis.com/auth/cloud-platform']
)

# Refresh the credentials to get the access token
credentials.refresh(Request())

# Get the access token from the credentials
access_token = credentials.token

# Define the headers including the Authorization header with the bearer token
headers = {
    'Authorization': f'Bearer {access_token}',
    'Content-Type': 'application/json'
}

# Make the request to the Cloud Run endpoint
response = requests.get(
    CLOUD_RUN_URL,
    headers=headers,
    # json=headers
)

# Print the response
print(response.status_code)
print(response.json())
