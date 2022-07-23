import time
import uuid

from sdk.utils.exceptions import AppAlreadyExistsException
from ..templates import Template


class Apps(Template):
    def __init__(self, token: str, warehouse_url: str) -> None:
        super().__init__(token, "datasets", "datasets", warehouse_url=warehouse_url)

    def create(
            self, name: str, account_id: str, project: str, db_type: str, db_connection_uri: str, tags: list = None,
            description: str = None
    ) -> dict:
        """
        The db_type can be:
            - mongodb
            - postgres
            - mysql
            etc...

        :param name:
        :type name:
        :param account_id:
        :type account_id:
        :param project:
        :type project:
        :param db_type:
        :type db_type:
        :param db_connection:
        :type db_connection:
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

                "database": {
                    "type": db_type,
                    "connectionUri": db_connection_uri,
                    "status": "testing"
                },

                "updatedAt": int(time.time()),
                "createdAt": int(time.time()),
            }
            self.db.insert([dataset])
            return dataset
        else:
            raise AppAlreadyExistsException
