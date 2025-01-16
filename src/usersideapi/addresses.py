from usersideapi.common import *

class address:
    class add_locality_type(action):
        def __init__(self,name,token):
            super().__init__()
            self.addparam('name',name)
            self.addparam('token',token)
    
    class edit_locality_type(action):
        def __init__(self,id):
            super().__init__()
            self.addparam('id',id)
        def name(self,name):
            self.addparam('name',name)
            return self
        def token(self,token):
            self.addparam('token',token)
    
    class get_locality_type(action):
        def __init__(self):
            super().__init__()
        def token(self,token):
            self.addparam('token', token)
            return self
    
    class get_alias(action):...

    class add_address(action):
        def __init__(self,locality_type_id,name):
            super().__init__()
            self.addparam('locality_type_id', locality_type_id)
            self.addparam('name', name)
        def parent_id(self,parent_id):
            self.addparam('parent_id', parent_id)
            return self
    
    class get(action):
        def __init__(self):
            super().__init__()
        def id(self,id):
            self.addparam('id', id)
            return self
        def locality_type_id(self,locality_type_id):
            self.addparam('locality_type_id', locality_type_id)
            return self
        def parent_id(self,parent_id):
            self.addparam('parent_id', parent_id)
            return self
        def is_disable_hidden(self,is_disable_hidden):
            self.addparam('is_disable_hidden', is_disable_hidden)
            return self
        
    class edit_address(action):
        def __init__(self,id):
            super().__init__()
            self.addparam('id', id)
        def map_color(self,map_color):
            self.addparam('map_color', map_color)
            return self
    
    class add_province(action):
        def __init__(self,name):
            super().__init__()
            self.addparam('name', name)

    class edit_province(action):
        def __init__(self,id):
            super().__init__()
            self.addparam('id', id)
        def name(self,name):
            self.addparam('name', name)
            return self
        
    class del_province(action):
        def __init__(self,id):
            super().__init__()
            self.addparam('id', id)
            
    class get_province(action):
        def __init__(self, id):
            super().__init__()
            if isinstance(id,list) or isinstance(id,tuple):
                s=str()
                for p in id: s+= f"{p},"
                self.addparam('id', s[:-1])
            else:
                self.addparam('id', id)
        # def __init__(self,id:int):
        #     super().__init__()
        #     self.addparam('id', id)