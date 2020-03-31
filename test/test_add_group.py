# -*- coding: utf-8 -*-
import pytest
from model.grroup import Group
from fixture.aplication import Aplication

@pytest.fixture
def app(request):
    fixture = Aplication()
    request.addfinalizer(fixture.destroy)
    return fixture

def test_add_group(app):
    app.session.login(username="admin", password="secret")
    app.group.create(Group(name="New group", header="Logo new", footer="Comment new"))
    app.session.logout()

def test_add_empty_group(app):
    app.session.login(username="admin", password="secret")
    app.group.create(Group(name="", header="", footer=""))
    app.session.logout()