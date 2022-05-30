import time
import uuid

from ..templates import Template


class Routes(Template):
    def __init__(self, token: str) -> None:
        super().__init__(token, "proxy", "routes")

    def create(self, account_id: str, project: str, service: str, config: dict) -> dict:
        """
        New Route flow
         1. create new route document
         2. trigger new route event
         3. proxy adds new config, if the given domain is accessible via that proxy
         4. proxy updates the route document
 
        @param account_id: 
        @param project: 
        @param service: 
        @param config: 
        @return: 
        """
        route = {
            "type": "route",
            "id": str(uuid.uuid4()),
            "accountId": account_id,
            "project": project,
            "service": service,
            "config": config,
            "updatedAt": int(time.time()),
            "createdAt": int(time.time()),

        }
        self.db.insert([route])
        return route
