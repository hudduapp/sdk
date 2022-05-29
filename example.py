from sdk.main import Data
from sdk.thirdparty.github import Github

# Example for data client
_d = Data("some_token")

res = _d.users.update({"login": "login"}, {"password": "...newPassword123"})
print(res)


# Example for github client
_g = Github("12345")
res = _g.get_repositories()  # get repos for current user

print(res)
