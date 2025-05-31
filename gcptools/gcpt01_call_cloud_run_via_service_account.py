from pathlib import Path
from mysecrets.mysecrets import endpoint_url, sa_json_path

import urllib.parse
import urllib.request

import google.auth.transport.requests
import google.oauth2.id_token
from google.oauth2 import service_account


def run_from_service_account(
        url: str,
        sa_json_path: Path
):
    SCOPES = ['https://www.googleapis.com/auth/cloud-platform']
    credentials = (
        service_account.Credentials.from_service_account_file(
            str(sa_json_path), scopes=SCOPES))
    request = google.auth.transport.requests.Request()

    credentials.refresh(request)
    oauth_token = credentials.token
    # headers = {'Authorization': f'Bearer {oauth_token}'}
    # request.h
    # response = requests.get(url, headers=headers)
    req = urllib.request.Request(url)
    req.add_header("Authorization", f"Bearer {oauth_token}")
    response = urllib.request.urlopen(req)
    return response.read()


if __name__ == "__main__":

    res = run_from_service_account(
        url=endpoint_url,
        sa_json_path=sa_json_path
    )

    print(res)
