from ..templates import Template


class Clusters(Template):
    """
    Clusters are a way to discover services
    """

    def __init__(self, token: str, collection: str = "workers") -> None:
        super().__init__(token, "clusters", collection)

    def register(self, node_id: str, merge: dict, config: dict) -> None:
        """
        A new item is only added if it doesn't exist already.

        Example::

        >>>     from sdk.data.clusters import Clusters
        >>>     from sdk.main import Data
        >>>
        >>>     _d = Data("data_token")
        >>>
        >>>     Clusters(_d.db.token, "cluster_name").register(
        >>>         "node_id", {"merge_data": "merge data gets merged with the cluster dict an 0 depth" } {"config_data": "as a dict"}
        >>>     )


        :param node_id:
        :type node_id:
        :param config:
        :type config:
        :param merge:
        :type merge:
        :return:
        :rtype:
        """
        cluster = {
            "type": self.collection,
            "nodeId": node_id,
            "config": config,
            "updatedAt": int(time.time()),
            **merge,
        }
        same_item_registered = self.db.retrieve({"nodeId": node_id})

        if not same_item_registered:
            cluster["id"] = str(uuid.uuid4())
            cluster["createdAt"] = int(time.time)
            cluster["token"] = str(secrets.token_hex(16))

            self.db.insert([cluster])
        else:
            # Update config data
            self.update({"nodeId": node_id}, cluster)

    def new_token(self, query: dict) -> dict:
        self.update({"nodeId": node_id}, {"token": str(secrets.token_hex(16))})

    def teardown(self, query: dict) -> None:
        """
        "Tear a cluster down"
        (Remove it from the clusters table)
        """
        self.db.delete(query)
