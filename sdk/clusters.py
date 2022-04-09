import time
import uuid
from .utils.data import (
    retrieve_documents,
    delete_documents,
    insert_documents,
    update_documents,
)


def register(node_id: str, region: str, api_endpoint: str) -> None:

    same_runner_registered = retrieve_documents(
        "clusters", "clusters", {"nodeId": node_id}
    )
    if not same_runner_registered:
        insert_documents(
            "clusters",
            "clusters",
            [
                {
                    "type": "runner",
                    "nodeId": node_id,
                    "region": region,
                    "apiEndpoint": api_endpoint,
                }
            ],
        )


def create_deployment(
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
    """
    Create a new deployment for an organization/user
    """

    insert_documents(
        "projects",
        "deployments",
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


def get_deployments(query: dict):
    res = []
    deployments = retrieve_documents("projects", "deployments", query)

    for project in deployments:
        del project["_id"]
        res.append(project)

    return res


def get_deployment(id: str):
    res = retrieve_documents("projects", "deployments", {"id": id})[0]
    del res["_id"]
    return res
