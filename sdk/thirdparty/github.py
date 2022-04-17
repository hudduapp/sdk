import requests
import json


class Github:
    def __init__(self, token: str) -> None:
        self.token = token
        self.headers = {"Authorization": f"Token {token}"}

    def get_current_github_user(self) -> dict:
        return requests.request(
            "GET", "https://api.github.com/user", headers=self.headers
        ).json()

    def get_repositories(self, query: dict = {}) -> dict:
        login = self.get_current_github_user()["login"]
        return requests.request(
            "GET",
            f"https://api.github.com/users/{login}/repos",
            params=json.dumps(query),
            headers=self.headers,
        ).json()

    def get_repository_branches(self, repo_name: str) -> dict:
        login = self.get_current_github_user()["login"]
        return requests.request(
            "GET",
            f"https://api.github.com/repos/{login}/{repo_name}/branches",
            headers=self.headers,
        ).json()
