from model.grroup import Group
from random import randrange


# def test_edit_group(app):
#     app.session.login(username="admin", password="secret")
#     app.group.edit_first_group(Group(name="Manya", header="Super", footer="Girl"))
#     app.session.logout()

def test_edit_group_name(app):
    if app.group.count() == 0:
        app.group.create(Group(name='test'))
    old_groups = app.group.get_group_list()
    index = randrange(len(old_groups))
    group = Group(name='Train')
    group.id = old_groups[index].id
    app.group.edit_group_by_index(index, group)
    assert len(old_groups) == app.group.count()
    new_groups = app.group.get_group_list()
    old_groups[index] = group
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)

# def test_edit_group_header(app):
#     old_groups = app.group.get_group_list()
#     if app.group.count() == 0:
#         app.group.create(Group(header='test'))
#     app.group.edit_first_group(Group(header='Submarine'))
#     new_groups = app.group.get_group_list()
#     assert len(old_groups) == len(new_groups)
