import secrets
import time
import uuid

from ..templates import Template


class Services(Template):

    def __init__(self, token: str, warehouse_url: str) -> None:
        super().__init__(token, "projects", "services", warehouse_url=warehouse_url)

    def create(
            self, name: str, project_id: str, account_id: str, config: dict = {}
    ) -> dict:
        service = {
            "type": "service",
            "id": str(uuid.uuid4()),
            "accountId": account_id,
            "name": name,
            "project": project_id,
            "updatedAt": int(time.time()),
            "createdAt": int(time.time()),
            "status": "CREATED",
            "token": secrets.token_hex(32),  # used on deployments for auth
            "config": config,  # config holds build_command pre_build_command etc...
        }
        self.db.insert([service])

        return service
