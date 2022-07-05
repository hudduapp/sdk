from .data.dataset import Datasets
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

        # accounts
        self.users = Users(self.warehouse_token, self.warehouse_url)

        # datasets
        self.datasets = Datasets(self.warehouse_token, self.warehouse_url)

    def health(self):
        return self.db.health()


class Events:
    def __init__(self, redis_uri: str):
        self.redis_uri = redis_uri
        self.queue = Queue(self.redis_uri)
