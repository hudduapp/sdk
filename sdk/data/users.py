import secrets
import time
import uuid

from ..templates import Template
from ..utils.exceptions import LoginAlreadyExistsException
from ..utils.hash import hash_password


class Users(Template):

    def __init__(self, token: str, warehouse_url: str) -> None:
        super().__init__(token, "accounts", "users", warehouse_url=warehouse_url)

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

                "updatedAt": int(time.time()),
                "createdAt": int(time.time()),
                # Settings
                "avatarUrl": None,
                # customization
                "username": login,
                "appearance": None,
                # payment
                "stripeUserId": None,
                "subscription": "free",
                # subscriptions:
                # 1. free: the default subscription
                # 2. pro: allows you to share unlimited dashboards & series
                "seatCount": 0  # how many users can be added to this account

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

    def recreate_workers_token(self, query: dict):
        self.update(
            query,
            {
                "integrationToken": str(secrets.token_bytes(16)),
                "integrationTokenExpires": int(time.time() + 60 * 60)
            }
        )
