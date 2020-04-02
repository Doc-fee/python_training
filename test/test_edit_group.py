from model.grroup import Group

def test_edit_group(app):
    app.session.login(username="admin", password="secret")
    app.group.edit_first_group(Group(name="Manya", header="Super", footer="Girl"))
    app.session.logout()