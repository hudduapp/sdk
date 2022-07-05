import secrets
import time
import uuid

from ..templates import Template
from ..utils.exceptions import ProjectNameAlreadyExistsException


class Datasets(Template):
    def __init__(self, token: str, warehouse_url: str) -> None:
        super().__init__(token, "datasets", "datasets", warehouse_url=warehouse_url)

    def create(
            self, name: str, account_id: str, apiUrl: str, apiVersion: float = 1, tags: list = None,
            description: str = None
    ) -> dict:
        """

        :param name:
        :type name:
        :param account_id:
        :type account_id:
        :param apiUrl:
        :type apiUrl:
        :param apiVersion:
        :type apiVersion:
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

                "apiUrl": apiUrl,
                "apiVersion": apiVersion,
                "apiToken": str(secrets.token_hex(16)),

                "tokens": [],

                "updatedAt": int(time.time()),
                "createdAt": int(time.time()),
            }
            self.db.insert([dataset])
            return dataset
        else:
            raise ProjectNameAlreadyExistsException

    def create_token(self, query: dict, scopes: list, expires: int = 0,
                     name: str = "unknown", token: str = secrets.token_hex(16)):
        token = {
            "name": name,
            "token": token,
            "scopes": scopes,
            "expires": expires,
            "createdAt": int(time.time())
        }
        tokens = self.get(query)["tokens"]
        tokens.append(token)
        self.update(
            query,
            {
                "tokens": tokens
            }
        )

    def delete_token(self, query: dict, token: str):
        tokens = self.get(query)["tokens"]
        token_to_remove = None
        for i in tokens:
            if i["token"] == token:
                token_to_remove = i
        tokens.remove(token_to_remove)
        self.update(
            query,
            {
                "tokens": tokens
            }
        )
