from usersideapi.common import *

class fiber:
    """API fiber
    Назначение: Кабельные линии 
    https://wiki.userside.eu/API_fiber"""
    class add(action):
        """Доработано в: 3.15.23 (добавлен параметры cableline_type_id)
        Описание: Добавление линии"""

        class objecttype(enum.auto):
            """Тип объекта (объект/здание)"""

            object = 'object_b_id'
            house = 'house_b_id'

        def __init__(self,object_a_id:int, object_b_id:int, object_b_type:objecttype = objecttype.object):
            """Обязательные параметры: object_a_id - ID начального объекта object_b_id - ID конечного объекта (либо house_b_id - ID конечного дома)"""

            super().__init__()
            self.addparam('object_a_id',object_a_id)
            self.addparam(object_b_type,object_b_id)

        def building_date(self,building_date):
            """building_date - Дата прокладки"""

            self.addparam('building_date',building_date)
            return self
        
        def building_length(self,building_length):
            """building_length - строительная длина"""

            self.addparam('building_length',building_length)
            return self
        
        def cableline_type_id(self,cableline_type_id):
            """cableline_type_id - ID типа кабельной линии"""

            self.addparam('cableline_type_id',cableline_type_id)
            return self
        
        def cabletype_id(self,cabletype_id):
            """cabletype_id - ID типа кабеля"""

            self.addparam('cabletype_id',cabletype_id)
            return self
        
        def comment(self,comment):
            """comment - Заметки"""
            
            self.addparam('comment',comment)
            return self
        
        def custom_color(self,custom_color):
            self.addparam('custom_color',custom_color)
            return self
        def fibers_count(self,fibers_count):
            self.addparam('fibers_count',fibers_count)
            return self
        def is_planned(self,is_planned):
            self.addparam('is_planned',is_planned)
            return self
        def is_change_color_by_cabletype(self,is_change_color_by_cabletype):
            self.addparam('is_change_color_by_cabletype',is_change_color_by_cabletype)
            return self
        def marking_a(self,marking_a):
            self.addparam('marking_a',marking_a)
            return self
        def marking_b(self,marking_b):
            self.addparam('marking_b',marking_b)
            return self
        # def object_a_id(self,object_a_id):
        #     self.addparam('object_a_id',object_a_id)
        #     return self
        # def object_b_id(self,object_b_id):
        #     self.addparam('object_b_id',object_b_id)
        #     return self
        def optical_length(self,optical_length):
            self.addparam('optical_length',optical_length)
            return self
    
    #class add_mark(action):
