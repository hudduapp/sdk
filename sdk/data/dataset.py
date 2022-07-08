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

    def run_query(self, query: dict):
        return requests.request(
            "POST", f"{self.dataset_url}/query", data=json.dumps(query), headers={
                "Content-Type": "application/json",
                "Authorization": f"Token {self.dataset_token}"
            }
        ).json()["items"]

    def upload_file(self, path):
        return requests.request(
            "POST", f"{self.dataset_url}/write", data=json.dumps({
                "file": open(path, "rb")
            }), headers={
                "Content-Type": "application/json",
                "Authorization": f"Token {self.dataset_token}"
            }
        ).json()

    def read_file(self, query: dict):
        return requests.request(
            "POST", f"{self.dataset_url}/read", data=json.dumps(query), headers={
                "Content-Type": "application/json",
                "Authorization": f"Token {self.dataset_token}"
            }
        )

    def create_raw_token(self, query: dict):
        return requests.request(
            "POST", f"{self.dataset_url}/raw", data=json.dumps(query), headers={
                "Content-Type": "application/json",
                "Authorization": f"Token {self.dataset_token}"
            }
        )
