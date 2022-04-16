from sdk.projects import Projects
from sdk.services import Services
from sdk.users import Users
from sdk.deployments import Deployments

from sdk.utils.data import WarehouseConnector


class Data:
    def __init__(self, token: str) -> None:
        outer_self = self
        self.token = token
        self.db = WarehouseConnector("dummy", "dummy", self.token)

        # projects
        self.projects = Projects(self.token)
        self.deployments = Deployments(self.token)
        self.services = Services(self.token)

        # accounts
        self.users = Users(self.token)
        # todo: orgs

        # clusters
        self.clusters = Cluster(self.token)

    def health(self):
        return self.db.health()
