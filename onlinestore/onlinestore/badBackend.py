from django.contrib.auth.backends import BaseBackend
from django.contrib.auth.models import User

class BadBackend(BaseBackend):
    """
    Backend for the bad hashing algo, should not really be used :)
    """

    def get_user(self, user_id):
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None

    def authenticate(self, request, username=None, password=None):
        try:
            return User.objects.get(username=username, password=password)
        except User.DoesNotExist:
            return None
