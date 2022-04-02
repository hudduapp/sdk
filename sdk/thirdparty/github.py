import requests
import json


def get_current_github_user(access_token: str) -> dict:
    headers = {"Authorization": f"Token {access_token}"}

    res = requests.request("GET", "https://api.github.com/user", headers=headers).json()
    return res


def get_repositories(access_token: str, query: dict = {}) -> dict:
    login = get_current_github_user(access_token)["login"]
    headers = {"Authorization": f"Token {access_token}"}
    res = requests.request(
        "GET",
        f"https://api.github.com/users/{login}/repos",
        params=json.dumps(query),
        headers=headers,
    ).json()

    return res
