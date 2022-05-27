from sdk.main import Data
from sdk.thirdparty.clusters_v1 import Cluster

_a = Cluster("http://localhost:5555")

# print(_a.create_deployment(
#     "echo hello",
#     "e07ed8d1-bfd5-492f-a1bd-61f363c2808b",  # account_id
#     "82ba1862-b7e1-416a-9574-13d4c9595d31",  # project
#     "12bc5098-59a1-4542-853c-37195a8e78ad",  # service
# ))

print(_a.get_deployments(limit=10))
