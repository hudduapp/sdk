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
