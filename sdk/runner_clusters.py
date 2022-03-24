import time
import secrets
import uuid
from .utils.data import retrieve_documents, delete_documents, insert_documents, update_documents
from .utils.exceptions import RunnersClusterNameAlreadyExistsException


def create_runners_cluster(name: str, account_type: str, account_login: str, account_avatar_url: str, tags: list = None, description: str = None):
    """
    Create a new runner_cluster for an organization/user
    """
    same_runner_cluster_name = bool(retrieve_documents(
        "runners", "clusters", {"name": name}))
    if not same_runner_cluster_name:
        insert_documents("runners", "clusters", [
            {
                "type": "runnerCluster",
                "id": str(uuid.uuid4()),
                "owner": {
                    "type": account_type,
                    "login": account_login,
                    "avatarUrl": account_avatar_url,
                    # "_comment": "Call the users endpoint for more information"
                },
                "name": name,
                "tags": tags,
                "description": description,
                "updatedAt": int(time.time()),
                "createdAt": int(time.time()),



                # settings
                "environment": {},  # default envvars
                "token": secrets.token_hex(20),

                "logActivityFor": ["newDeployment", "deleteDeployment", "updateSettings"]
            }
        ])

    else:
        raise RunnersClusterNameAlreadyExistsException


def get_runners_cluster(id: str):
    res = retrieve_documents(
        "runners", "clusters", {"id": id})[0]
    del res["_id"]
    res["environment"] = [k for k, _v in res["environment"].items()]
    res["deploymentTriggerWebhooks"] = [
        k for k, _v in res["deploymentTriggerWebhooks"].items()]
    return res


def update_runners_cluster(login: str, **kwargs) -> None:
    runner_cluster = get_runner_cluster(login)
    new_data = {**runner_cluster, **kwargs}

    update_documents("runners", "clusters", {
                     "login": login}, {"$set": new_data})
