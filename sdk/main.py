from .data.clusters import Clusters
from .data.deployments import Deployments
from .data.projects import Projects
from .data.queue import Queue
from .data.routes import Routes
from .data.services import Services
from .data.tokens import Tokens
from .data.users import Users
from .utils.data import WarehouseConnector


class Data:
    def __init__(self, warehouse_token: str, warehouse_url: str = "https://data.huddu.io") -> None:
        self.warehouse_token = warehouse_token
        self.warehouse_url = warehouse_url
        self.redis_uri = redis_uri

        self.db = WarehouseConnector("dummy", "dummy", self.warehouse_token)

        # internal use only
        self.warehouse_tokens = Tokens(self.warehouse_token)

        # projects
        self.projects = Projects(self.warehouse_token)
        self.deployments = Deployments(self.warehouse_token)
        self.services = Services(self.warehouse_token)

        # router
        self.routes = Routes(self.warehouse_token)

        # accounts
        self.users = Users(self.warehouse_token)
        # todo: orgs

        # clusters
        self.clusters = Clusters(self.warehouse_token)

    def health(self):
        return self.db.health()


class Events:
    def __init__(self, redis_uri: str):
        self.redis_uri = redis_uri
        self.queue = Queue(self.redis_uri)
