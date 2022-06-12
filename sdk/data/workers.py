import secrets
import time
import uuid

from ..templates import Template
from ..utils.exceptions import WorkerNameAlreadyExistsException


class Workers(Template):
    def __init__(self, token: str) -> None:
        super().__init__(token, "workers", "workers")

    def create(
        self,
        node_id: str,
        account_id: str,
        config: dict,
        route: str = None,
        status: str = "IDLE",
    ) -> dict:
        """

        :param node_id:
        :type node_id:
        :param account_id:
        :type account_id:
        :param route:
        :type route:
        :param config:
        :type config:
        :param status:
        :type status:
        :return:
        :rtype:
        """
        same_worker_name = bool(self.db.retrieve({"nodeId": node_id}))
        if not same_worker_name:
            worker = {
                "type": "worker",
                "id": str(uuid.uuid4()),
                "accountId": account_id,
                "route": route,
                "nodeId": node_id,
                "status": status.upper(),
                "config": config,
                "token": str(secrets.token_hex(16)),
                "updatedAt": int(time.time()),
                "createdAt": int(time.time()),
            }
            self.db.insert([worker])
            return worker
        else:
            raise WorkerNameAlreadyExistsException
