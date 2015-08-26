from memcache import Client
from uuid import uuid4

class SessionHandler:
    inst = None
    def __init__(self):
        SessionHandler.inst = self
        self.conn = Client(["127.0.0.1:11211"])

    def setuid(self, uid):
        key = uuid4().get_hex()
        self.conn.set(key, uid, 3600)
        return key

    def getuid(self, key):
        return self.conn.get(key)
        
    def deluid(self, key):
        self.conn.delete(key)
