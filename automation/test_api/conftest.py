#Standard library imports.
import requests


#Related third party imports.
import pytest


#Local application/library specific imports.  



@pytest.fixture
def get_session():
    session = requests.session()
    return session