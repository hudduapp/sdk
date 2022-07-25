from .data.activity import Activity
from .data.dashboards import Dashboards
from .data.project_tokens import ProjectTokens
from .data.projects import Projects
from .data.queue import Queue
from .data.series import Series
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
        self.project_tokens = ProjectTokens(self.warehouse_token, self.warehouse_url)

        # accounts
        self.users = Users(self.warehouse_token, self.warehouse_url)

        # series
        self.series = Series(self.warehouse_token, self.warehouse_url)

        # events
        self.activity = Activity(self.warehouse_token, self.warehouse_url)

        # dashboards
        self.dashboards = Dashboards(self.warehouse_token, self.warehouse_url)


def health(self):
    return self.db.health()


class Events:
    def __init__(self, redis_uri: str):
        self.redis_uri = redis_uri
        self.queue = Queue(self.redis_uri)
