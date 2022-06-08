# Responses
class DbConnectionRequiredException(Exception):
    pass


class InvalidPermissionsException(Exception):
    """
    The applied token does not have the required permissions to access the requested resource
    """

    pass


# Users
class LoginAlreadyExistsException(Exception):
    pass


# Projects
class ProjectNameAlreadyExistsException(Exception):
    pass


# Workers
class WorkerNameAlreadyExistsException(Exception):
    pass
