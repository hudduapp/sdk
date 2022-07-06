import secrets
import time
import uuid

from ..templates import Template
from ..utils.exceptions import ProjectNameAlreadyExistsException


class Datasets(Template):
    def __init__(self, token: str, warehouse_url: str) -> None:
        super().__init__(token, "datasets", "datasets", warehouse_url=warehouse_url)

    def create(
            self, name: str, account_id: str, api_url: str, api_token: str = str(secrets.token_hex(16)),
            tags: list = None,
            description: str = None
    ) -> dict:
        """

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
            """
             Tokens should look something like this:
             [
                 {
                     "accountId": "token_account_id",
                     "token":token, 
                     "read":bool,
                     "write":bool,
                     "delete":bool
                 }
             ]
             """
            dataset = {
                "type": "dataset",
                "id": str(uuid.uuid4()),
                "accountId": account_id,
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
            raise ProjectNameAlreadyExistsException
