import time
import uuid

from .templates import Template
from .utils.data import WarehouseConnector
from .utils.exceptions import ProjectNameAlreadyExistsException


class Projects(Template):
    def __init__(self, token: str) -> None:
        super().__init__(token, "projects", "projects")

    def create(
        self,
        name: str,
        account_id: str,
        tags: list = None,
        description: str = None,
        git_provider: str = None,
        repository: str = None,
        branch: str = None,
        deploy_on: list = [],
        config: dict = {},
    ) -> dict:
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
                # source code from where exactly?!
                "gitProvider": git_provider,
                "repository": repository,
                "branch": branch,
                "deployOn": deploy_on,
                "config": config,  # or local config
                # settings
                "runnerClusters": [],
                "environment": {},
                "deploymentTriggerWebhooks": [],
                "previewImage": None,
                "publicUrl": None,
                "domains": [],
                "deploymentHooks": {},
                "logActivityFor": [
                    "newDeployment",
                    "deleteDeployment",
                    "updateSettings",
                ],
            }
            self.db.insert([project])
            return project
        else:
            raise ProjectNameAlreadyExistsException
