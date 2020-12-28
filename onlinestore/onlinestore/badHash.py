from django.contrib.auth.hashers import BasePasswordHasher
# from django.utils.crypto import constant_time_compare

class BadHasher(BasePasswordHasher):
    """
    Hasher that should never EVER be used for anything, as it does not do anything :)
    """

    algorithm = "BadHasher"

    def encode(self, password, salt, iterations=None):
        assert password is not None
        return password

    def verify(self, password, encoded):
        return password == encoded

    def safe_summary(self, encoded):
        return { 'password': encoded }
