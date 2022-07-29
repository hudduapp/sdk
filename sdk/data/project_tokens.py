import secrets
import time
import uuid

from ..templates import Template


class ProjectTokens(Template):
    def __init__(self, token: str, warehouse_url: str) -> None:
        super().__init__(token, "projects", "tokens", warehouse_url=warehouse_url)

    def create(
            self, name: str, account_id: str, project: str, scopes: list, series: list, description: str = None,
            expires: int = 0
    ) -> dict:
        project_token = {
            "type": "projectToken",
            "id": str(uuid.uuid4()),
            "accountId": account_id,
            "name": name,
            "description": description,
            "token": str(secrets.token_hex(16)),
            "scopes": scopes,
            "series": series,  # series == pl of series
            "expires": expires,
            "createdAt": int(time.time()),
        }
        self.db.insert([project_token])
        return project_token
