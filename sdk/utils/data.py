import requests
import json


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
        requests.request(
            "POST",
            f"{self.base_url}/databases/{self.database}/collections/{self.collection}",
            data=json.dumps({"documents": documents}),
            headers=self.headers,
        )

    def delete(self, query: dict) -> None:
        requests.request(
            "POST",
            f"{self.base_url}/databases/{self.database}/collections/{self.collection}",
            data=json.dumps({"query": query}),
            headers=self.headers,
        )

    def retrieve(self, query: dict) -> list:
        return requests.request(
            "GET",
            f"{self.base_url}/databases/{self.database}/collections/{self.collection}",
            data=json.dumps({"query": query}),
            headers=self.headers,
        ).json()["items"]

    def update(self, query: dict, update: dict) -> None:
        res = requests.request(
            "PUT",
            f"{self.base_url}/databases/{self.database}/collections/{self.collection}",
            data=json.dumps({"query": query, "update": update}),
            headers=self.headers,
        )
