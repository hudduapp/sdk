import time
import uuid
import secrets

from ..templates import Template
from ..utils.exceptions import ProjectNameAlreadyExistsException


class AuthTokens(Template):
    def __init__(self, token: str) -> None:
        super().__init__(token, "authentication", "tokens")

    def create(
        self,
        account_id: str,
        description: str = None,
        expires_at: int = None,
        meta: dict = {},
    ) -> dict:
        token = {
            "type": "token",
            "id": str(uuid.uuid4()),
            "accountId": account_id,
            "token": secrets.token_hex(32),
            "description": description,
            "meta": meta,
            "expiresAt": expires_at,
            "createdAt": int(time.time()),
        }
        self.db.insert([token])
        return token
