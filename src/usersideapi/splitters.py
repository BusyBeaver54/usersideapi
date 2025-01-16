from usersideapi.common import *

class splitter:
    class get(action):
        def __init__(self):
            super().__init__()
        def id(self,id):
            self.addparam(self.id.__name__,id)
            return self
        
    class add(action):
        def __init__(self,node_id,port_count_in,port_count_out):
            super().__init__()
            self.addparam('node_id',node_id)
            self.addparam('port_count_in',port_count_in)
            self.addparam('port_count_out',port_count_out)
        def description(self,description):
            self.addparam('description',description)
            return self
        def is_planned(self,is_planned):
            self.addparam('is_planned',is_planned)
            return self
        
    class edit(action):
        def __init__(self,id):
            super().__init__()
            self.addparam('id',id)
        def description(self,description):
            self.addparam('description',description)
            print(self.__dict__)
            return self
        def is_planned(self,is_planned):
            self.addparam('is_planned',is_planned)
            return self

    class delete(action):
        def __init__(self,id):
            super().__init__()
            self.addparam('id',id)