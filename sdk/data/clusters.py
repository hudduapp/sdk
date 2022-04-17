import time
import uuid

from ..templates import Template


class Clusters(Template):
    def __init__(self, token: str) -> None:
        super().__init__(token, "clusters", "clusters")

    def register(self, node_id: str, region: str, api_endpoint: str) -> dict:
        """
        Only registers a cluster if it doesn't already exist
        """

        same_runner_registered = self.db.retieve({"nodeId": node_id})

        if not same_runner_registered:
            cluster = {
                "type": "cluster",
                "nodeId": node_id,
                "region": region,
                "apiEndpoint": api_endpoint,
            }
            self.db.insert([cluster])

    def teardown(self, query: dict) -> None:
        """
        "Tear a cluster down"
        (Remove it from the clusters table)
        """
        self.db.delete(query)
