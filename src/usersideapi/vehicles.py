from usersideapi.common import *

class vehicle:
    class get(action):

        def __init__(self):
            super().__init__()
            
        def id(self,id):
            self.addparam(self.id.__name__,id)
            return self