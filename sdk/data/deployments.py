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
            node_id: str,
            current_deployment: bool,
            config: dict
    ) -> dict:
        """
        Deployment flow:
        1. New deployment created on dashboard or by a git integration
        2. Queue event sent (via Events redis integration)
        3. Deployment event received by cluster -> create deployment
        4. Update deployment in database to match new deployment info on cluster

        IMPORTANT: The node_id is what decides where a deployment will be deployed

        Info to add on the cluster (guideline):
        1. containerId
        2. clusterId
        3. logsUrl (should be url + token)
        4. (maybe) artifactsUrl (should be url + token)
        5. exposed ports

        @param name:
        @param account_id:
        @param project:
        @param service:
        @param current_deployment:
        @param config:
        @return:
        """
        deployment = {
            "type": "deployment",
            "id": str(uuid.uuid4()),
            "accountId": account_id,
            "project": project,
            "service": service,
            "node_id": node_id,

            "currentDeployment": current_deployment,
            "name": name,
            "config": config,
            "createdAt": int(time.time()),
            "updatedAt": int(time.time()),

        }
        self.db.insert(
            [deployment],
        )
        return deployment
