import time
import uuid

from ..templates import Template


class Series(Template):
    def __init__(self, token: str, warehouse_url: str) -> None:
        super().__init__(token, "apps", "apps", warehouse_url=warehouse_url)

    def create(
            self, name: str, account_id: str, project: str, meta: dict
    ) -> dict:
        """
        Meta will hold all the information about how to display this series

        :param name:
        :param account_id:
        :param project:
        :param meta:
        :return:
        """

        app = {
            "type": "app",
            "id": str(uuid.uuid4()),
            "accountId": account_id,
            "project": project,
            "name": name,
            "meta": meta,
            "updatedAt": int(time.time()),
            "createdAt": int(time.time())
        }
        self.db.insert([app])
        return app
