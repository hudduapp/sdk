import json

import requests


class Cluster:
    def __init__(self, url: str):
        self.url = url

    def _request(self, method: str, path: str, data=None, params=None) -> dict:
        if params is None:
            params = {}
        if data is None:
            data = {}

        return requests.request(
            method,
            f"{self.url}{path}",
            data=json.dumps(data),
            params=params,
            headers={"Content-Type": "application/json"},
        ).json()

    # create
    def create_deployment(
            self,
            build_command: str,
            account_id: str,
            project: str,
            service: str,
            expose: object = None,
            environment: object = None,
            pre_build_command: str = "",
            image: str = "ubuntu:latest",
            name: str = "unknown",
    ) -> dict:
        if expose is None:
            expose = []
        if environment is None:
            environment = {}

        return self._request(
            "POST",
            "/deployments",
            data={
                "preBuildCommand": pre_build_command,
                "buildCommand": build_command,
                "image": image,
                "expose": expose,
                "environment": environment,
                "accountId": account_id,
                "project": project,
                "service": service,
                "name": name,
            },
        )

    def redeploy_deployment(
            self,
            deployment_id: str
    ):

        return self._request(
            "POST",
            f"/deployments/{deployment_id}/redeploy"
        )

    # retrieve
    def get_deployments(
            self,
            service: str = None,
            project: str = None,
            limit: int = 25,
            skip: int = 0,
    ):

        return self._request(
            "GET",
            "/deployments",
            params={
                "service": service,
                "project": project,
                "limit": limit,
                "skip": skip
            },
        )

    def get_deployment(
            self,
            deployment_id: str
    ):

        return self._request(
            "GET",
            f"/deployments/{deployment_id}"
        )

    # delete
    def delete_deployment(
            self,
            deployment_id: str
    ):

        return self._request(
            "DELETE",
            f"/deployments/{deployment_id}"
        )
