from usersideapi.common import *

class node:
    class add(action):
        def __init__(self,type:int):
            super(action,self).__init__()
            self.addparam('type',type)
        def city_id(self,city_id:int) : 
            self.addparam(self.city_id.__name__, city_id)
            return self
        def custom_icon_id(self,custom_icon_id:int) : 
            self.addparam(self.custom_icon_id.__name__, custom_icon_id)
            return self
        def comment(self,comment) : 
            self.addparam(self.comment.__name__, comment)
            return self
        def date_add(self,date_add) : 
            self.addparam(self.date_add.__name__, date_add)
            return self
        def entrance(self,entrance) : 
            self.addparam(self.entrance.__name__, entrance)
            return self
        def house_id(self,house_id:int) : 
            self.addparam(self.house_id.__name__, house_id)
            return self
        def inventory_number(self,inventory_number) : 
            self.addparam(self.inventory_number.__name__, inventory_number)
            return self
        def is_planned(self,is_planned) : 
            self.addparam(self.is_planned.__name__, is_planned)
            return self
        def level(self,level) : 
            self.addparam(self.level.__name__, level)
            return self
        def level_id(self,level_id:int) : 
            self.addparam(self.level_id.__name__, level_id)
            return self
        def location(self,location) : 
            self.addparam(self.location.__name__, location)
            return self
        def node_parent_id(self,node_parent_id) : 
            self.addparam(self.node_parent_id.__name__, node_parent_id)
            return self
        def number(self,number) : 
            self.addparam(self.number.__name__, number)
            return self
        def owner_id(self,owner_id) : 
            self.addparam(self.owner_id.__name__, owner_id)
            return self
        # def map_id(self,map_id) : 
        #     self.addparam(self.map_id.__name__, map_id)
        #     return self
        def coordinates(self,coordinates) : 
            self.addparam(self.coordinates.__name__, coordinates)
            return self
    class add_mark(action):
        def __init__(self,node_id,mark_id):
            super().__init__()
            self.addparam('node_id',node_id)
            self.addparam('mark_id',mark_id)
    class change_custom_icon(action):
        def __init__(self,id,custom_icon_id):
            super().__init__()
            self.addparam('id',id)
            self.addparam('custom_icon_id',custom_icon_id)
    class delete(action):
        def __init__(self,id):
            super().__init__()
            self.addparam('id',id)
    class delete_mark(action):
        def __init__(self,node_id,mark_id):
            super().__init__()
            self.addparam('node_id',node_id)
            self.addparam('mark_id',mark_id)
    class edit(action):
        def __init__(self,id):
            super().__init__()
            self.addparam('id',id)
        def city_id(self,city_id):
            self.addparam('city_id',city_id)
            return self
        def custom_icon_id(self,custom_icon_id):
            self.addparam('custom_icon_id',custom_icon_id)
            return self
        def comment(self,comment):
            self.addparam('comment',comment)
            return self
        def coordinates(self,coordinates):
            self.addparam('coordinates',coordinates)
            return self
        def date_add(self,date_add):
            self.addparam('date_add',date_add)
            return self
        def entrance(self,entrance):
            self.addparam('entrance',entrance)
            return self
        def house_id(self,house_id):
            self.addparam('house_id',house_id)
            return self
        def inventory_number(self,inventory_number):
            self.addparam('inventory_number',inventory_number)
            return self
        def is_planned(self,is_planned):
            self.addparam('is_planned',is_planned)
            return self
        def level(self,level):
            self.addparam('level',level)
            return self
        def level_id(self,level_id):
            self.addparam('level_id',level_id)
            return self
        def location(self,location):
            self.addparam('location',location)
            return self
        def node_parent_id(self,node_parent_id):
            self.addparam('node_parent_id',node_parent_id)
            return self
        def number(self,number):
            self.addparam('number',number)
            return self
        def owner_id(self,owner_id):
            self.addparam('owner_id',owner_id)
            return self

    class get(action):
        def __init__(self):
            super().__init__()
        def address_id(self,address_id) : 
            self.addparam(self.address_id.__name__, address_id)
            return self
        def city_id(self,city_id) : 
            self.addparam(self.city_id.__name__, city_id)
            return self
        def entrance_number(self,entrance_number) : 
            self.addparam(self.entrance_number.__name__, entrance_number)
            return self
        def house_id(self,house_id) : 
            self.addparam(self.house_id.__name__, house_id)
            return self
        def id(self,id) : 
            self.addparam('id', id)
            return self
        def mark_id(self,mark_id) : 
            self.addparam(self.mark_id.__name__, mark_id)
            return self
        def object_type(self,object_type) : 
            self.addparam(self.object_type.__name__, object_type)
            return self
        def parent_id(self,parent_id) : 
            self.addparam(self.parent_id.__name__, parent_id)
            return self
        def street_id(self,street_id) : 
            self.addparam(self.street_id.__name__, street_id)
            return self

    class get_icon_list(action):
        def __init__(self):
            super().__init__()
        def id(self,id) : 
            self.addparam(self.id.__name__, id)
            return self

    class get_id(action):
        def __init__(self,data_type,data_value):
            super().__init__()
            self.addparam('data_type', data_type)
            self.addparam('data_value', data_value)
        def is_entry(self,is_entry) : 
            self.addparam(self.is_entry.__name__, is_entry)
            return self
        def type_id(self,type_id) : 
            self.addparam(self.type_id.__name__, type_id)
            return self
        
    class get_id_by_coord(action):
        def __init__(self,lat,lon):
            super().__init__()
            self.addparam('lat', lat)
            self.addparam('lon', lon)
        def type(self,type) : 
            self.addparam(self.type.__name__, type)
            return self
        def range(self,range) : 
            self.addparam(self.range.__name__, range)
            return self
        
    class get_redevelopment_scheme(action):
        def __init__(self,id):
            super().__init__()
            self.addparam('id', id)

    class get_scheme(action):
        def __init__(self,id):
            super().__init__()
            self.addparam('id', id)
        
    class get_type_list(action):...

class Node(usObject):

    __apply_immediately = True

    def __init__(self,id = None):
        if id == None:
            self.as_dict()
        else:
            props = node.get().id(id).request().as_json()
            if props['result'] != eOk():
                raise exception('Invalid data', props)
            else:
                self.__usprops = props['data'][f'{id}']
                del props
                # self.__param = tpl('Node',(),param['data'][str(id)])
                super().__init__(self.__usprops['id'])
                self.__set_address_id(self.__usprops['address_id'])
                self.__date_add = self.__usprops['date_add']
                self.__entrance = self.__usprops['entrance']
                self.__level = self.__usprops['level']
                self.__level_id = self.__usprops['level_id']
                self.__parent_id = self.__usprops['parent_id']
                self.__is_planned = self.__usprops['is_planned']
                self.__location = self.__usprops['location']
                self.__comment = self.__usprops['comment']
                self.__name = self.__usprops['name']
                self.__set_type(self.__usprops['type'])
                self.__custom_icon_id = self.__usprops['custom_icon_id']
                self.__number = self.__usprops['number']
                self.__coordinates = self.__usprops['coordinates']


    def __get_type(self):
        return self.__type
    
    def __set_type(self,val):
            self.__type = val
    
    def __get_address_id(self):
        return self.__address_id
    
    def __set_address_id(self,val):
        self.__address_id = val

    def __get_number(self):
        return self.__number

    def __set_number(self,val):
        if self.applyImmediately:
            res = node.edit(self.id).number(val).request().as_json()
            if not ErrorStatus.isOk(res['result']):
                raise exception(f'Invalid data set {self.number.__name__}', res)
        self.__number = val

    type = property(__get_type,__set_type)
    """ID типа объекта
    https://wiki.userside.eu/API_node#get_type_list"""
    
    address_id = property(__get_address_id,__set_address_id)
    """ID адресной единицы 
    result[data][address_id]
    Изменить можно только через методы city_id или house_id
    https://wiki.userside.eu/API_node#edit"""

    number = property(__get_number,__set_number)
    """Номер объекта
    https://wiki.userside.eu/API_node#get_type_list"""

    def __getattr__(self, val):
        return None

    def __eq__(self,other)->bool:
        """Сравнение объектов Node по всем текущим свойствам.
        Если у одного из изначально одинаковых объектов изменить любое свойство без применения в US, результат будет False"""
        if other.__class__.__name__ != self.__class__.__name__: 
            raise exception('Incompatible type', other.__class__.__name__)
        return self.as_dict() == other.as_dict()
    
    def __ne__(self,other)->bool:
        """Сравнение объектов Node по всем текущим свойствам.
        Если у одного из изначально одинаковых объектов изменить любое свойство без применения в US, результат будет True"""
        if other.__class__.__name__ != self.__class__.__name__: 
            raise exception('Incompatible type', other.__class__.__name__)
        return not self.__eq__(other)
    
    def as_dict(self):
        return {'id':self.id,
              'address_id':self.address_id,
              'date_add':self.__date_add,
              'entrance':self.__entrance,
              'level':self.__level,
              'level_id':self.__level_id,
              'parent_id':self.__parent_id,
              'is_planned':self.__is_planned,
              'location':self.__location,
              'comment':self.__comment,
              'name':self.__name,
              'type':self.__type,
              'custom_icon_id':self.__custom_icon_id,
              'number':self.__number,
              'coordinates':self.__coordinates}

    def __str__(self):
        return str(self.as_dict())
    
    def __set_apply_prop_immediately(self, val:bool):
        self.__apply_immediately = val

    def __get_apply_prop_immediately(self)->bool:
        return self.__apply_immediately
    
    apply_prop_immediately = property(__get_apply_prop_immediately,__set_apply_prop_immediately)

    def confirm_changes(self):pass


    @staticmethod
    def get_icon_list()->dict:
        resdict = node.get_icon_list().request().as_json()
        if resdict['result'] == 'OK':
            return resdict['data']

    @staticmethod
    def get_type_list()->dict:
        resdict = node.get_type_list().request().as_json()
        if resdict['result'] == 'OK':
            return resdict['data']

    # @number.getter
    # def getnumber(self):
    #     return self.number