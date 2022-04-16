import time
import uuid

from .templates import Template


class Services(Template):
    def __init__(self, token: str) -> None:
        super().__init__(token, "projects", "services")

    def create(
        self, name: str, project_id: str, account_id: str, config: dict = {}
    ) -> dict:
        service = {
            "type": "service",
            "id": str(uuid.uuid4()),
            "accountId": account_id,
            "name": name,
            "project": project_id,
            "deployment": None,
            "updatedAt": int(time.time()),
            "createdAt": int(time.time()),
            "status": "CREATED",
            "currentDeployment": None,
            "config": config,
        }
        self.db.insert([service])

        return service
