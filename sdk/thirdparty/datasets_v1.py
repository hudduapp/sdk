import json
import secrets
from typing import List

import requests


class Datasets:
    def __init__(self, dataset_url: str, dataset_token: str):
        self.dataset_token = dataset_token
        self.dataset_url = dataset_url

    def create_token(self, scopes: List[str], expires: int = 0, token: str = secrets.token_hex(16)):
        requests.request(
            "POST", f"{self.dataset_url}/tokens", headers={
                "Authorization": f"Token {self.dataset_token}"
            },
            data=json.dumps({
                "token": token,
                "scopes": scopes,
                "expires": expires
            })
        )

    def delete_token(self, token: str):
        requests.request(
            "DELETE", f"{self.dataset_url}/tokens", headers={
                "Authorization": f"Token {self.dataset_token}"
            },
            data=json.dumps({
                "token": token
            })
        )
