import requests


def get_current_github_user(access_token):
    headers = {"Authorization": f"Token {access_token}"}

    res = requests.request("GET", "https://api.github.com/user", headers=headers).json()

    return res
