from model.grroup import Group

# def test_edit_group(app):
#     app.session.login(username="admin", password="secret")
#     app.group.edit_first_group(Group(name="Manya", header="Super", footer="Girl"))
#     app.session.logout()

def test_edit_group_name(app):
    if app.group.count() == 0:
        app.group.create(Group(name='test'))
    app.group.edit_first_group(Group(name='Train'))

def test_edit_group_header(app):
    if app.group.count() == 0:
        app.group.create(Group(header='test'))
    app.group.edit_first_group(Group(header='Submarine'))
