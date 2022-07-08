import json
import secrets
from typing import List

import requests
from requests import Response


class DatasetManager:
    def __init__(self, dataset_url: str, dataset_token: str):
        self.dataset_token = dataset_token
        self.dataset_url = dataset_url

    def create_token(self, name: str, scopes: List[str], expires: int = 0, token: str = secrets.token_hex(16)):
        requests.request(
            "POST", f"{self.dataset_url}/tokens", headers={
                "Content-Type": "application/json",
                "Authorization": f"Token {self.dataset_token}"
            },
            data=json.dumps({
                "token": token,
                "scopes": scopes,
                "expires": expires,
                "name": name
            })
        )

    def delete_token(self, token: str):
        requests.request(
            "DELETE", f"{self.dataset_url}/tokens", headers={
                "Content-Type": "application/json",
                "Authorization": f"Token {self.dataset_token}"
            },
            data=json.dumps({
                "token": token
            })
        )


class DatasetConsumerLite:
    def __init__(self, dataset_url: str, dataset_token: str):
        self.dataset_token = dataset_token
        self.dataset_url = dataset_url

    def ping_cluster(self) -> Response:
        return requests.request(
            "GET", f"{self.dataset_url}/info", headers={
                "Content-Type": "application/json",
                "Authorization": f"Token {self.dataset_token}"
            }
        ).json()

    def run_query(self, data: dict):
        return requests.request(
            "POST", f"{self.dataset_url}/query", data=data, headers={
                "Content-Type": "application/json",
                "Authorization": f"Token {self.dataset_token}"
            }
        ).json()
