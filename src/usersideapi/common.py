import enum
import json
import requests
from requests.exceptions import HTTPError
from pathlib import Path
import tempfile
import shutil
import datetime as dt

getRespName = lambda: f'response_{dt.datetime.now():%Y%m%d_%H%M%S%f}.json'

class ErrorStatus(enum.auto):
    eOk =               0
    eNotInitValue =     0x01
    eNotConnection =    0x02
    eBadRequest =       0x04
    eBadDataResponse =  0x08
    eInvalidId =        0x10
    eIncompatibleData = 0x20
    @staticmethod
    def isOk(response):
        return response == 'OK'

def eOk(): return 'OK'
sES = {'eOk':eOk}

def errorStatusText(es:str):
    return sES.get(es)

class exception(Exception):
    def __init__(self, text:str, status):
        self.text = text
        self.status = status

class tpl(type):
    def __new__(cls, name, bases, dict, **kwargs):
        return type.__new__(cls, name, bases, dict)
    def __init__(cls, name, bases, dict, **kwargs):
        return super(tpl, cls).__init__(name, bases, dict)

class apiserver(tpl('url', (), { 'host' : None, 'port' : 443, 'apiscr' : 'api.php', 'apikey' : None})):
    @staticmethod
    def url(): return f'https://{apiserver.host}:{apiserver.port}/{apiserver.apiscr}?key={apiserver.apikey}'


def simple_request(str:str):
    return requests.get(f'https://{apiserver.host}:{apiserver.port}/{apiserver.apiscr}?key={apiserver.apikey}&{str}')

class request(apiserver):
    response = None
    _action = None
    def __init_subclass__(cls):
        cls._action = cls
    def __init__(self):
            self.uri={}
    def __str__(self):
        url = self.url()
        if self._action:
            url += f"&cat={self._action.__module__.rsplit('.')[-1]}&action={self._action.__name__}"
        if len(self.uri):
            for par in self.uri.keys():
                url += f"&{par}={self.uri[par]}"
        return url
    def addparam(self,key:str,val):
        self.uri[key] = str(val)
        return self
    def request(self):
        self.response = requests.get(self.__str__())
        code = self.response.status_code
        if code != 200:
            if code == 403:
                raise exception('Forbidden http:403', f'check apiserver.apikey: {apiserver.apikey}')
            else:
                raise exception('Request error', f'http:{code}')

        self.temp_dir = tempfile.gettempdir()+'\\UserSideApi'
        if not Path(self.temp_dir).exists(): Path(self.temp_dir).mkdir()
        temp_file_path = self.temp_dir + '\\' + getRespName()
        with open(temp_file_path,'w') as file:
            file.write(self.response.text)
        return self
    
    def as_text(self)->str:
        return self.response.text
    
    def as_json(self)->dict:
        data = self.response.content.decode()
        return json.loads(data)
    
    def __del__(self):
        if self.response: 
            self.response.close()
        # if hasattr(self,'temp_dir'): shutil.rmtree(self.temp_dir)

class action(request):...

class usObject():

    def __init__(self,id):
        self.__set_id(id)

    def __get_id(self):
        return self.__id
    
    def __set_id(self,id):
        if id == None: return
        if id > 0:
            self.__id = id
        else:
            raise exception('Invalidate ID. Must be > 0', f'id:{id}')
        
    id = property(__get_id,__set_id)
    """ID объекта"""

    def __getattr__(self, val):
        return None