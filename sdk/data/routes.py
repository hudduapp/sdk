import time
import uuid

from ..templates import Template


class Routes(Template):
    def __init__(self, token: str) -> None:
        super().__init__(token, "router", "routes")

    def create(self, account_id: str, config: dict) -> dict:
        """
        trying to query for changes?
        1. watch for db triggers
        2. retrieve all new documents updatedAt after x (bad practice)
        @param account_id:
        @param config:
        @return:
        """
        user = {
            "type": "user",
            "id": str(uuid.uuid4()),
            "accountId": account_id,
            "config": config,
            "updatedAt": int(time.time()),
            "createdAt": int(time.time()),

        }
        self.db.insert([user])
        return user
