
import pytest
from fixture.aplication import Aplication

fixture = None


@pytest.fixture
def app(request):
    global fixture
    if fixture is None:
        fixture = Aplication()
    else:
        if not fixture.is_valid():
            fixture = Aplication()
    fixture.session.ensure_login(username="admin", password="secret")
    return fixture

@pytest.fixture(scope='session', autouse=True)
def stoop(request):
    def fin():
        fixture.session.ensure_logout()
        fixture.destroy()
    request.addfinalizer(fin)
    return fixture
