class LoginAlreadyExistsException(Exception):
    pass


class InavlidPasswordException(Exception):
    pass


class UserDoesNotExistException(Exception):
    pass


class CannotDeleteUserException(Exception):
    pass


# Projects

class ProjectNameAlreadyExistsException(Exception):
    pass


# Clusters + Runners
class RunnersClusterNameAlreadyExistsException(Exception):
    pass
