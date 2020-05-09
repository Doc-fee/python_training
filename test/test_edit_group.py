from model.grroup import Group
import random


# def test_edit_group(app):
#     app.session.login(username="admin", password="secret")
#     app.group.edit_first_group(Group(name="Manya", header="Super", footer="Girl"))
#     app.session.logout()

def test_edit_group_name(app, db, check_ui):
    if len(db.get_group_list()) == 0:
        app.group.create(Group(name='test'))
    old_groups = db.get_group_list()
    group = random.choice(old_groups)
    groupname = Group(name='Train')
    groupname.id = group.id
    app.group.edit_group_by_id(group.id, groupname)
#   assert len(old_groups) == app.group.count()
    new_groups = db.get_group_list()
    index = 0
    for item in old_groups:
        if item.id == group.id:
            old_groups[index] = groupname
        index += 1
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
    if check_ui:
        assert sorted(new_groups, key=Group.id_or_max) == sorted(app.group.get_group_list(), key=Group.id_or_max)



# def test_edit_group_header(app):
#     old_groups = app.group.get_group_list()
#     if app.group.count() == 0:
#         app.group.create(Group(header='test'))
#     app.group.edit_first_group(Group(header='Submarine'))
#     new_groups = app.group.get_group_list()
#     assert len(old_groups) == len(new_groups)
