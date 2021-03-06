import time
import uuid

from ..templates import Template


class Series(Template):
    def __init__(self, token: str, warehouse_url: str) -> None:
        super().__init__(token, "series", "series", warehouse_url=warehouse_url)

    def create(
            self, name: str, account_id: str, project: str, dashboard: str, meta: dict = {}
            , description: str = None) -> dict:
        """
        Meta will hold all the information about how to display this series

        NOTE: series are not saved in the huddu db instead they are saved via the data-api

        :param name:
        :param account_id:
        :param project:
        :param meta:
        :param dashboard
        :param description
        :return:
        """

        series = {
            "type": "series",
            "id": str(uuid.uuid4()),
            "accountId": account_id,
            "project": project,
            "dashboard": dashboard,
            "name": name,
            "description": description,
            "meta": meta,
            "updatedAt": int(time.time()),
            "createdAt": int(time.time())
        }
        self.db.insert([series])
        return series
