from sdk.main import Data
from pymongo import MongoClient

a = Data("12345")

# b = a.projects.get({"name": "My Project"})

# c = a.projects.create("demo2", "e07ed8d1-bfd5-492f-a1bd-61f363c2808b")

# c = a.projects.list({"id": "82ba1862-b7e1-416a-9574-13d4c9595d31"})
# c = a.deployments.get({"project": "82ba1862-b7e1-416a-9574-13d4c9595d31"})
#
c = a.users.update({"login": "dab"}, {"password": ".Sommer1"})
# c = a.health()
print(c)
