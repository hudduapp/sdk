import time
import uuid

from ..templates import Template


class Dashboards(Template):
    def __init__(self, token: str, warehouse_url: str) -> None:
        super().__init__(token, "dashboards", "dashboards", warehouse_url=warehouse_url)

    def create(
            self, name: str, account_id: str, project: str, meta: dict, tags: list = None, description: str = None
    ) -> dict:
        """
        
        :param name:
        :param account_id:
        :param meta:
        :param tags:
        :param description:
        :param project
        :return:
        """

        dashboard = {
            "type": "dashboard",
            "id": str(uuid.uuid4()),
            "accountId": account_id,
            "project": project,
            "name": name,
            "tags": tags,
            "description": description,
            "meta": meta,
            "updatedAt": int(time.time()),
            "createdAt": int(time.time()),
        }
        self.db.insert([dashboard])
        return dashboard
