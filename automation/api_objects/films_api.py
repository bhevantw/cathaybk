#Standard library imports.
import logging

#Related third party imports.


#Local application/library specific imports.  
from utils.api_base import *


class Films(APIBase):

    def __init__(self, session):
        self.session = session
    
    def send(self, method, id=None):
        if id:
            self.url = f"https://swapi.dev/api/films/{id}/"
        else:
            self.url = f"https://swapi.dev/api/films/"
        self.api_request(method)
    
