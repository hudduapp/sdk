from sdk.thirdparty.proxy import Proxy

_a = Proxy(
    "some_token")

# print(_a.create_deployment(
#     "echo hello",
#     "e07ed8d1-bfd5-492f-a1bd-61f363c2808b",  # account_id
#     "82ba1862-b7e1-416a-9574-13d4c9595d31",  # project
#     "12bc5098-59a1-4542-853c-37195a8e78ad",  # service
# ))

print(_a.create_or_update_proxy_route())
