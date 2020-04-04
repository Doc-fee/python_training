
import pytest
from fixture.aplication import Aplication

@pytest.fixture
def app(request):
    fixture = Aplication()
    request.addfinalizer(fixture.destroy)
    return fixture
