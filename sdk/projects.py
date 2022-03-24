import time
import uuid
from .utils.data import retrieve_documents, delete_documents, insert_documents, update_documents
from .utils.exceptions import ProjectNameAlreadyExistsException


def create_project(name: str, account_id: str, tags: list = None, description: str = None):
    """
    Create a new project for an organization/user
    """
    same_project_name = bool(retrieve_documents(
        "projects", "projects", {"name": name}))
    if not same_project_name:
        insert_documents("projects", "projects", [
            {
                "type": "project",
                "id": str(uuid.uuid4()),
                "accountId": account_id,
                # "owner": {
                #    "type": account_type,
                #    "login": account_login,
                #    "avatarUrl": account_avatar_url,
                #    # "_comment": "Call the users endpoint for more information"
                # },
                "name": name,
                "tags": tags,
                "description": description,
                "updatedAt": int(time.time()),
                "createdAt": int(time.time()),



                # settings
                "runnerClusters": [],
                "environment": {},
                "deploymentTriggerWebhooks": [],
                "previewImage": None,
                "publicUrl": None,

                "domains":[],
                "deploymentHooks":{},

                "logActivityFor": ["newDeployment", "deleteDeployment", "updateSettings"],
            }
        ])

    else:
        raise ProjectNameAlreadyExistsException


def get_projects(account_id: str, return_secret_data: bool = False):
    res = []
    projects = retrieve_documents("projects", "projects", {
                                  "accountId": account_id})

    for project in projects:
        del project["_id"]

        if not return_secret_data:
            project["environment"] = [
                k for k, _v in project["environment"].items()]
            project["deploymentTriggerWebhooks"] = [
                k for k, _v in project["deploymentTriggerWebhooks"].items()]
        res.append(project)

    return res


def get_project(id: str, return_secret_data: bool = False):
    res = retrieve_documents(
        "projects", "projects", {"id": id})[0]
    del res["_id"]

    if not return_secret_data:
        res["environment"] = [k for k, _v in res["environment"].items()]
        res["deploymentTriggerWebhooks"] = [
            k for k, _v in res["deploymentTriggerWebhooks"].items()]

    return res


def update_project(id: str, **kwargs) -> None:
    project = get_project(id)
    new_data = {**project, **kwargs}

    update_documents("projects", "projects", {
                     "id": id}, {"$set": new_data})
