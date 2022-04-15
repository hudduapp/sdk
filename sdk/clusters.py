import time
import uuid
from .utils.data import (
    retrieve_documents,
    delete_documents,
    insert_documents,
    update_documents,
)


class Clusters:
    def __init__(self, token: str):
        self.db = WarehouseConnector("clusters", "clusters", token=token)
        self.token = token

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

    def list(self, query: dict) -> list:
        res = []
        clusters = self.db.retrieve(query)

        for cluster in clusters:
            del cluster["_id"]
            res.append(cluster)

        return res

    def get(self, query: dict) -> dict:
        res = self.db.retrieve(query)[0]
        del res["_id"]

        return res
