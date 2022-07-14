from .utils.data import WarehouseConnector
from .utils.exceptions import DbConnectionRequiredException


class Template:
    def __init__(
            self, token: str, database: str, collection: str, schema=lambda: {},
            warehouse_url: str = "https://data.huddu.io"
    ) -> None:
        if not collection or not database:
            raise DbConnectionRequiredException
        else:
            self.db = WarehouseConnector(database, collection, token, warehouse_url)
        self.token = token
        self.schema = schema
        self.collection = collection
        self.database = database
        self.warehouse_url = warehouse_url

    def create(self, args: dict) -> dict:
        """
        Dummy method.
        Feel free to create your own method
        """
        item = {**args, **self.schema()}
        self.db.insert([item])
        return item

    def list(self, query: dict, sort=None, limit: int = 25, skip: int = 0) -> list:
        if sort is None:
            sort = {}
        res = []
        items = self.db.retrieve(query, sort=sort, limit=limit, skip=skip)

        for item in items:
            del item["_id"]
            res.append(item)

        return res

    def get(self, query: dict) -> dict:
        res = self.db.retrieve(query)[0]
        del res["_id"]

        return res

    def update(self, query: dict, update: dict) -> dict:
        item = self.get(query)
        new_data = {**item, **update}

        self.db.update(query, {"$set": new_data})
        return new_data

    def delete(self, query: dict) -> None:
        self.db.delete(query)
