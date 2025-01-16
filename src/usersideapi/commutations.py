from usersideapi.common import *

class commutation:
    class add(action):
        class objecttype_1(enum.auto):
            customer='customer'
            switch='switch'
            fiber='fiber'
            cross='cross'
            splitter='splitter'
        class objecttype_2(enum.auto):
            switch='switch'
            fiber='fiber'
            cross='cross'
            splitter='splitter'
        def __init__(self, object_type : objecttype_1, object_id : int, object1_side, object1_port, object2_type : objecttype_2, object2_id : int, object2_side, object2_port):
            super().__init__()
            self.addparam('object_type',object_type)
            self.addparam('object_id',object_id)
            self.addparam('object1_side',object1_side)
            self.addparam('object1_port',object1_port)
            self.addparam('object2_type',object2_type)
            self.addparam('object2_id',object2_id)
            self.addparam('object2_side',object2_side)
            self.addparam('object2_port',object2_port)
    
    class delete(action):
        class objecttype(enum.auto):
            customer='customer'
            switch='device'
        def __init__(self, object_type : objecttype, object_id : int):
            super().__init__()
            self.addparam('object_type',object_type)
            self.addparam('object_id',object_id)
        def object_port(self,object_port):
            self.addparam('object_port',object_port)
            return self
        
    class get_data(action):
        class objecttype(enum.auto):
            customer='customer'
            switch='switch'
            radio='radio'
            cross='cross'
            fiber='fiber'
            splitter='splitter'
        def __init__(self, object_type : objecttype):
            super().__init__()
            self.addparam('object_type',object_type)
        def object_id(self,object_id):
            self.addparam('object_id',object_id)
            return self
        def is_finish_data(self,is_finish_data):
            self.addparam('is_finish_data',is_finish_data)
            return self