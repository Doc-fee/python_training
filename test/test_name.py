def test_name_home_page(app):
    name_from_home_page = app.contact.get_contact_list()[0]
    name_from_edit_page = app.contact.get_contact_info_from_edit_page(0)
    assert name_from_home_page.name == name_from_edit_page.name

def test_lastname_home_page(app):
    lastname_from_home_page = app.contact.get_contact_list()[0]
    lastname_from_edit_page = app.contact.get_contact_info_from_edit_page(0)
    assert lastname_from_home_page.lastname == lastname_from_edit_page.lastname

