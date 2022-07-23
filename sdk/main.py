from .data.activity import Activity
from .data.app_tokens import AppTokens
from .data.apps import Apps
from .data.projects import Projects
from .data.queue import Queue
from .data.tokens import Tokens
from .data.users import Users
from .utils.data import WarehouseConnector


class Data:
    def __init__(self, warehouse_token: str, warehouse_url: str = "https://data.huddu.io") -> None:
        self.warehouse_token = warehouse_token
        self.warehouse_url = warehouse_url

        self.db = WarehouseConnector("dummy", "dummy", self.warehouse_token, self.warehouse_url)

        # internal use only
        self.warehouse_tokens = Tokens(self.warehouse_token, self.warehouse_url)

        # projects
        self.projects = Projects(self.warehouse_token, self.warehouse_url)

        # accounts
        self.users = Users(self.warehouse_token, self.warehouse_url)

        # apps
        self.apps = Apps(self.warehouse_token, self.warehouse_url)
        self.app_tokens = AppTokens(self.warehouse_token, self.warehouse_url)

        # events
        self.activity = Activity(self.warehouse_token, self.warehouse_url)


def health(self):
    return self.db.health()


class Events:
    def __init__(self, redis_uri: str):
        self.redis_uri = redis_uri
        self.queue = Queue(self.redis_uri)
