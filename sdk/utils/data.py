import json

import requests

from .exceptions import InvalidPermissionsException


class WarehouseConnector:
    def __init__(
            self,
            database: str,
            collection: str,
            token: str,
            base_url: str = "https://data.huddu.io",
    ) -> None:
        self.token = token
        self.base_url = base_url
        self.database = database
        self.collection = collection
        self.headers = {
            "Authorization": f"Token {token}",
            "Content-Type": "application/json",
        }

    def insert(self, documents: list) -> None:
        try:
            requests.request(
                "POST",
                f"{self.base_url}/databases/{self.database}/collections/{self.collection}",
                data=json.dumps({"documents": documents}),
                headers=self.headers,
            )
        except:
            raise InvalidPermissionsException

    def delete(self, query: dict) -> None:
        try:
            requests.request(
                "POST",
                f"{self.base_url}/databases/{self.database}/collections/{self.collection}",
                data=json.dumps({"query": query}),
                headers=self.headers,
            )
        except:
            raise InvalidPermissionsException

    def retrieve(self, query: dict, limit: int = 25, skip: int = 0) -> list:
        try:
            return requests.request(
                "GET",
                f"{self.base_url}/databases/{self.database}/collections/{self.collection}",
                data=json.dumps({"query": query, "limit": limit, "skip": skip}),
                headers=self.headers,
            ).json()["items"]
        except:
            raise InvalidPermissionsException

    def update(self, query: dict, update: dict) -> None:
        try:
            requests.request(
                "PUT",
                f"{self.base_url}/databases/{self.database}/collections/{self.collection}",
                data=json.dumps({"query": query, "update": update}),
                headers=self.headers,
            )
        except:
            raise InvalidPermissionsException

    def health(self) -> dict:
        return requests.request(
            "GET",
            f"{self.base_url}/health",
            headers=self.headers,
        ).json()
