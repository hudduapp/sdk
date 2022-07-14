import json
import secrets
import time
import uuid

import requests
from requests import Response

from sdk.utils.exceptions import DatasetAlreadyExistsException
from ..templates import Template


class Datasets(Template):
    def __init__(self, token: str, warehouse_url: str) -> None:
        super().__init__(token, "datasets", "datasets", warehouse_url=warehouse_url)

    def create(
            self, name: str, account_id: str, project: str, api_url: str, api_token: str = str(secrets.token_hex(16)),
            tags: list = None,
            description: str = None
    ) -> dict:
        """
        :param project:
        :type project:
        :param name:
        :type name:
        :param account_id:
        :type account_id:
        :param api_url:
        :type api_url:
        :param api_token:
        :type api_token:
        :param tags:
        :type tags:
        :param description:
        :type description:
        :return:
        :rtype:
        """
        same_dataset_name = bool(self.db.retrieve({"name": name}))
        if not same_dataset_name:
            dataset = {
                "type": "dataset",
                "id": str(uuid.uuid4()),
                "accountId": account_id,
                "project": project,
                "name": name,
                "tags": tags,
                "description": description,

                "apiUrl": api_url,
                "apiToken": api_token,

                "updatedAt": int(time.time()),
                "createdAt": int(time.time()),
            }
            self.db.insert([dataset])
            return dataset
        else:
            raise DatasetAlreadyExistsException


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
        ).json()
