import requests


class Github:
    def __init__(self, token: str) -> None:
        self.token = token
        self.headers = {"Authorization": f"Token {token}"}

    def get_current_github_user(self) -> dict:
        return requests.request(
            "GET", "https://api.github.com/user", headers=self.headers
        ).json()

    def search(self, path: str, query: dict):
        login = self.get_current_github_user()["login"]
        return requests.request(
            "GET",
            f"https://api.github.com/search{path}",
            params=query,
            headers=self.headers,
        ).json()
