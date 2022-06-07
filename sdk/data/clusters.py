from ..templates import Template


class Clusters(Template):
    """
    Clusters are a way to discover services
    """

    def __init__(self, token: str, collection: str = "workers") -> None:
        super().__init__(token, "clusters", collection)

    def register(self, node_id: str, meta: dict) -> None:
        """
        A new item is only added if it doesn't exist already.

        Example::

        >>>     from sdk.data.clusters import Clusters
        >>>     from sdk.main import Data
        >>>
        >>>     _d = Data("data_token")
        >>>
        >>>     Clusters(_d.db.token, "cluster_name").register(
        >>>         "node_id", {"meta_data": "as a dict"}
        >>>     )


        :param node_id:
        :type node_id:
        :param meta:
        :type meta:
        :return:
        :rtype:
        """
        same_item_registered = self.db.retrieve({"nodeId": node_id})

        if not same_item_registered:
            cluster = {
                "type": self.collection,
                "nodeId": node_id,
                "meta": meta
            }
            self.db.insert([cluster])
        else:
            # Update meta data
            self.update(
                {
                    "nodeId": node_id
                },
                {
                    "meta": meta
                }
            )

    def teardown(self, query: dict) -> None:
        """
        "Tear a cluster down"
        (Remove it from the clusters table)
        """
        self.db.delete(query)
