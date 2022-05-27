from sdk.thirdparty.clusters_v1 import Cluster

_a = Cluster("abcde", "http://localhost:5555")

# print(_a.create_deployment(
#     "echo hello",
#     "e07ed8d1-bfd5-492f-a1bd-61f363c2808b",  # account_id
#     "82ba1862-b7e1-416a-9574-13d4c9595d31",  # project
#     "12bc5098-59a1-4542-853c-37195a8e78ad",  # service
# ))

print(_a.get_deployment("b7df4d9d-0e41-474c-9041-a95ac75187eb"))
