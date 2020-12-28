from django.contrib.sessions.backends.db import SessionStore as OriginalSessionStore
import random

class SessionStore(OriginalSessionStore):
    """ A terrible session store :) """
    def _get_new_session_key(self):
        while True:
            session_key = str(random.randint(10000000, 100000000))
            if not self.exists(session_key):
                break
        return session_key
