import time
import uuid
from .utils.data import (
    retrieve_documents,
    delete_documents,
    insert_documents,
    update_documents,
)


def create_deployment(
    name: str,
    account_id: str,
    build_command: str,
    pre_build_command: str,
    node_id: str,
    region: str,
    environment: dict,
    expose: dict,
):
    """
    Create a new runner_cluster for an organization/user
    """

    insert_documents(
        "projects",
        "deployments",
        [
            {
                "type": "deployment",
                "id": str(uuid.uuid4()),
                "accountId": account_id,
                "name": name,
                "updatedAt": int(time.time()),
                "createdAt": int(time.time()),
                "environment": {},
                "expose": expose,
            }
        ],
    )


def get_deployment(id: str):
    res = retrieve_documents("projects", "deployments", {"id": id})[0]
    del res["_id"]
    return res
