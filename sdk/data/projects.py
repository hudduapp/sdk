import time
import uuid

from ..templates import Template
from ..utils.exceptions import ProjectNameAlreadyExistsException


class Projects(Template):
    def __init__(self, token: str, warehouse_url: str) -> None:
        super().__init__(token, "projects", "projects", warehouse_url=warehouse_url)

    def create(
            self, name: str, account_id: str, tags: list = None, description: str = None
    ) -> dict:
        """
        @param name:
        @param account_id:
        @param tags:
        @param description:
        @return:
        """
        same_project_name = bool(self.db.retrieve({"name": name}))
        if not same_project_name:
            project = {
                "type": "project",
                "id": str(uuid.uuid4()),
                "accountId": account_id,
                "name": name,
                "tags": tags,
                "description": description,
                "updatedAt": int(time.time()),
                "createdAt": int(time.time()),
            }
            self.db.insert([project])
            return project
        else:
            raise ProjectNameAlreadyExistsException
