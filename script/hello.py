import sys
import os
class hello:
    def GET(self, name):
        return str(os.getpid())
