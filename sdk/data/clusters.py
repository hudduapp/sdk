import time
import uuid

from ..templates import Template


class Clusters(Template):
    def __init__(self, token: str) -> None:
        super().__init__(token, "clusters", "clusters")

    def register(self, node_id: str, region: str, base_url: str, version: str) -> None:
        """
        Only registers a cluster if it doesn't already exist
        """

        same_runner_registered = self.db.retrieve({"nodeId": node_id})

        if not same_runner_registered:
            cluster = {
                "type": "cluster",
                "nodeId": node_id,
                "region": region,
                "baseUrl": base_url,
                "version": version
            }
            self.db.insert([cluster])

    def teardown(self, query: dict) -> None:
        """
        "Tear a cluster down"
        (Remove it from the clusters table)
        """
        self.db.delete(query)
