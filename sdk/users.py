import time
import uuid
from .utils.data import WarehouseConnector
from .utils.hash import hash_password
from .utils.exceptions import LoginAlreadyExistsException
from .templates import Template


class Users(Template):
    def __init__(self, token: str) -> None:
        super().__init__(token, "accounts", "users")

    def create(self, login: str, password: str, email: str) -> dict:
        same_login_name = bool(self.db.retrieve({"login": login}))
        if not same_login_name:
            user = {
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
                "stripeUserId": None,
            }
            self.db.insert([user])
            return user
        else:
            raise LoginAlreadyExistsException

    def update(self, query: dict, update: dict) -> dict:
        user = self.get(query)
        new_data = {**user, **update}

        if "password" in update:
            new_data["password"] = hash_password(update["password"]).decode("utf-8")

        self.db.update(query, {"$set": new_data})
        return new_data
