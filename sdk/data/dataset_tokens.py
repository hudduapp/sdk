import secrets
import time
import uuid
from typing import List

from .dataset import Datasets
from ..templates import Template
from ..thirdparty.datasets_v1 import DatasetManager


class DatasetTokens(Template):
    def __init__(self, token: str, warehouse_url: str) -> None:
        super().__init__(token, "datasets", "tokens", warehouse_url=warehouse_url)
        self._datasets = Datasets(self.token, self.warehouse_url)

    def create(
            self, dataset: str, scopes: List[str], expires: int = 0, token: str = str(secrets.token_hex(16)),
            name: str = "unknown",
            meta: dict = {}
    ) -> dict:
        token_entry = {
            "type": "datasetToken",
            "id": str(uuid.uuid4()),
            "name": name,
            "dataset": dataset,
            "scopes": scopes,
            "expires": expires,
            "token": token,

            "createdAt": int(time.time()),
        }
        self.db.insert([token_entry])

        dataset = self._datasets.get({
            "id": dataset
        })
        dataset_manager = DatasetManager(
            dataset["apiUrl"],
            dataset["apiToken"],
        )
        dataset_manager.create_token(
            name,
            scopes,
            expires=expires,
            token=token
        )

        return token_entry

    def delete(self, query: dict):
        self.db.delete(query)

        token = self.get(query)
        dataset = self._datasets.get(
            {"id": token["dataset"]}
        )
        dataset_manager = DatasetManager(
            dataset["apiUrl"],
            dataset["apiToken"],
        )
        dataset_manager.delete_token(
            token["token"]
        )
