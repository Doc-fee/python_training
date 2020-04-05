# -*- coding: utf-8 -*-
from model.grroup import Group


def test_add_group(app):
    app.group.create(Group(name="New group", header="Logo new", footer="Comment new"))

def test_add_empty_group(app):
    app.group.create(Group(name="", header="", footer=""))
