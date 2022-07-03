import time
import uuid

from ..templates import Template
from ..utils.exceptions import ProjectNameAlreadyExistsException


class Datasets(Template):
    def __init__(self, token: str, warehouse_url: str) -> None:
        super().__init__(token, "datasets", "datasets", warehouse_url=warehouse_url)

    def create(
            self, name: str, account_id: str, apiEndpoint: str, apiVersion: float = 1, tags: list = None,
            description: str = None
    ) -> dict:
        """
        @param name:
        @param account_id:
        @param tags:
        @param description:
        @return:
        """
        same_dataset_name = bool(self.db.retrieve({"name": name}))
        if not same_dataset_name:
            dataset = {
                "type": "dataset",
                "id": str(uuid.uuid4()),
                "accountId": account_id,
                "name": name,
                "tags": tags,
                "description": description,

                "apiEndpoint": apiEndpoint,
                "apiVersion": apiVersion,

                "tokens": {},

                "updatedAt": int(time.time()),
                "createdAt": int(time.time()),
            }
            self.db.insert([dataset])
            return dataset
        else:
            raise ProjectNameAlreadyExistsException
