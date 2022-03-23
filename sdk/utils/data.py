import requests
import json

_base_url = "https://data.huddu.io"
_headers = {
    "Authorization": "abcde",
    "Content-Type": "application/json"
}


def insert_documents(database: str, collection: str, documents: list) -> None:
    requests.request("POST", f"{_base_url}/databases/{database}/collections/{collection}",  data=json.dumps(
        {"documents": documents}), headers=_headers)


def delete_documents(database: str, collection: str, query: dict) -> None:
    requests.request("POST", f"{_base_url}/databases/{database}/collections/{collection}", data=json.dumps(
        {"query": query}), headers=_headers)


def retrieve_documents(database: str, collection: str, query: dict) -> None:
    return requests.request("GET", f"{_base_url}/databases/{database}/collections/{collection}", data=json.dumps(
        {"query": query}), headers=_headers).json()["items"]


def update_documents(database: str, collection: str, query: dict, update: dict) -> None:
    print(json.dumps(
        {"query": query, "update": update}))
    res = requests.request("PUT", f"{_base_url}/databases/{database}/collections/{collection}", data=json.dumps(
        {"query": query, "update": update}), headers=_headers)
    print(res.json())
