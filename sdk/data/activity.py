import time
import uuid

from ..templates import Template


class Activity(Template):
    def __init__(self, token: str, warehouse_url: str) -> None:
        super().__init__(token, "activity", "activity", warehouse_url=warehouse_url)

    def create(
            self, event: str, account_id: str, meta: dict = {}
    ) -> dict:
        """

        :param event:
        :type event:
        :param account_id:
        :type account_id:
        :param meta:
        :type meta:
        :return:
        :rtype:
        """

        activity = {
            "type": "activity",
            "id": str(uuid.uuid4()),
            "accountId": account_id,
            "event": event,
            "meta": meta,
            "createdAt": int(time.time()),
        }
        self.db.insert([activity])
        return activity
