import secrets
import time
import uuid

from ..templates import Template


class Tokens(Template):
    def __init__(self, token: str, warehouse_url: str) -> None:
        super().__init__(token, "authentication", "tokens", warehouse_url=warehouse_url)

    def create(
            self,
            account_id: str,
            description: str = None,
            scopes: list = [],
            expires_at: int = None,
            meta: dict = {},
    ) -> dict:
        token = {
            "type": "token",
            "id": str(uuid.uuid4()),
            "accountId": account_id,
            "token": secrets.token_hex(32),
            "description": description,
            "scopes": scopes,
            "meta": meta,
            "expiresAt": expires_at,
            "createdAt": int(time.time()),
        }
        self.db.insert([token])
        return token
