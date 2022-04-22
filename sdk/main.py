from .data.projects import Projects
from .data.services import Services
from .data.users import Users
from .data.deployments import Deployments
from .data.clusters import Clusters
from .data.tokens import Tokens

from .utils.data import WarehouseConnector


class Data:
    def __init__(self, token: str) -> None:
        outer_self = self
        self.token = token
        self.db = WarehouseConnector("dummy", "dummy", self.token)

        # internal use only
        self.tokens = Tokens(self.tokens)

        # projects
        self.projects = Projects(self.token)
        self.deployments = Deployments(self.token)
        self.services = Services(self.token)

        # accounts
        self.users = Users(self.token)
        # todo: orgs

        # clusters
        self.clusters = Clusters(self.token)

    def health(self):
        return self.db.health()
