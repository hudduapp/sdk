import secrets
import time
import uuid
from typing import List

from ..templates import Template


class AppTokens(Template):
    def __init__(self, token: str, warehouse_url: str) -> None:
        super().__init__(token, "apps", "tokens", warehouse_url=warehouse_url)

    def create(
            self, app: str, scopes: List[str], expires: int = 0, token: str = str(secrets.token_hex(16)),
            name: str = "unknown",
            meta: dict = {}
    ) -> dict:
        token_entry = {
            "type": "appToken",
            "id": str(uuid.uuid4()),
            "name": name,
            "app": app,
            "scopes": scopes,
            "expires": expires,
            "token": token,

            "createdAt": int(time.time()),
        }
        self.db.insert([token_entry])

        return token_entry
