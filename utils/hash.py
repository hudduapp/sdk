import bcrypt


def hash_password(password: str) -> str:
    """
    Hash a password and return the hashed string using bcrypt
    """
    return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt(12))


def validate_password(plain_password: str, hashed_password: str) -> bool:
    return bcrypt.checkpw(plain_password, hashed_password)
