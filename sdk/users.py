import time
from .utils.data import retrieve_documents, delete_documents, insert_documents, update_documents
from .utils.hash import hash_password
from .utils.exceptions import InavlidPasswordException, LoginAlreadyExistsException, UserDoesNotExistException, CannotDeleteUserException


def create_user(login: str, password: str, email: str) -> None:
    """
    Create a new user for specified login, password and email.
    """

    same_login_name = bool(retrieve_documents(
        "accounts", "users", {"login": login}))
    if not same_login_name:
        insert_documents("accounts", "users", [
            {
                "type": "user",
                "id": str(uuid.uuid4()),
                "login": login,
                "password": hash_password(password).decode("utf-8"),
                # account info
                "email": email,
                "verified": False,
                "emailVerificationId": str(uuid.uuid4()),
                "updatedAt": int(time.time()),
                "createdAt": int(time.time()),

                # Settings
                # notifications
                "defaultNotificationsEmail": email,
                "sendNotificationFor": ["newActivity"],
                "totalProjects": 0,
                "totalRunners": 0,
                "avatarUrl": None,
                # customization
                "username": login,
                "language": None,
                "appearance": None,
                # automization
                "githubAccountToken": None,
                "gitlabAccountToken": None,
                "bitbucketAccountToken": None,
                # payment
                "stripeUserId": None

            }])

    else:
        raise LoginAlreadyExistsException


def get_user(login: str) -> dict:

    res = retrieve_documents(
        "accounts", "users", {"login": login})[0]
    del res["_id"]  # yes this is required.
    del res["password"]
    return res


def update_user(login: str, **kwargs) -> None:
    user = get_user(login)
    new_data = {**user, **kwargs}

    if "password" in kwargs:
        new_data["password"] = hash_password(
            kwargs["password"]).decode("utf-8")

    update_documents("accounts", "users", {"login": login}, {"$set": new_data})


def delete_user(login: str) -> None:
    user = get_user(login)
    if (user["totalRunners"] == 0) and (user["totalProjects"] == 0):
        delete_documents("accounts", "users", {"login": login})
    else:
        raise CannotDeleteUserException
