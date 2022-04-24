import time
import uuid

from ..templates import Template


class Deployments(Template):
    def __init__(self, token: str) -> None:
        super().__init__(token, "projects", "deployments")

    def create(
        self,
        name: str,
        account_id: str,
        project: str,
        service: str,
        build_command: str,
        pre_build_command: str,
        node_id: str,
        container_id: str,
        region: str,
        environment: dict,
        expose: dict,
    ) -> None:
        deployment = {
            "type": "deployment",
            "id": str(uuid.uuid4()),
            "accountId": account_id,
            "project": project,
            "service": service,
            "name": name,
            "containerId": container_id,
            "region": region,
            "nodeId": node_id,
            "buildCommand": build_command,
            "preBuildCommand": pre_build_command,
            "environment": {},
            "expose": expose,
            "createdAt": int(time.time()),
        }
        self.db.insert(
            [deployment],
        )
        return deployment
