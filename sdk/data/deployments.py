import time
import uuid

from ..templates import Template


class Deployments(Template):
    def __init__(self, token: str) -> None:
        super().__init__(token, "projects", "deployments")

    def create(
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
        self.db.insert(
            [
                {
                    "type": "deployment",
                    "id": str(uuid.uuid4()),
                    "accountId": account_id,
                    "project": project,
                    "service": service,
                    "name": name,
                    "createdAt": int(time.time()),
                    "containerId": container_id,
                    "environment": {},
                    "expose": expose,
                }
            ],
        )

    def list(self, query: dict) -> list:
        res = []
        deployments = self.db.retrieve(query)

        for deployment in deployments:
            del deployment["_id"]
            res.append(deployment)

        return res

    def get(self, query: dict) -> dict:
        res = self.db.retrieve(query)[0]
        del res["_id"]

        return res

    def update(self, query: dict, update: dict) -> dict:
        deployment = self.get(query)
        new_data = {**deployment, **update}

        self.db.update(query, {"$set": new_data})
        return new_data

    def delete(self, query: dict) -> None:
        self.db.delete(query)
