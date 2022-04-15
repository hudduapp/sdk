from sdk.projects import Projects
from sdk.services import Services
from sdk.users import Users
from sdk.deployments import Deployments


class Data:
    def __init__(self, token: str) -> None:
        outer_self = self
        self.token = token
        self.deployments = Deployments(self.token)
        self.projects = Projects(self.token)
