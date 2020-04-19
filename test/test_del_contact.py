from model.contact import Contact


def test_delete_first_contact(app):
    if app.contact.count() == 0:
        app.contact.add_contact_form(Contact(name = "Boris", middlename = "Mc", lastname = "Smith", nickname = "Gus", title = "-",company = "IT", address = "Atlantida",
                 homephone = "5556677", mobile='7775558899', work="4182369", fax = "4569632", email="kloun@mail.ru", email2="-", email3="-", homepage="-", bday="5",
                 bmonth="January", byear="2000", address2="world", phone2="7418526", notes="-"))
        app.contact.submit()
        app.contact.return_home_page()
    old_contacts = app.contact.get_contact_list()
    app.contact.delete_first_contact()
    assert len(old_contacts) - 1 == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts[0:1] = []
    assert old_contacts == new_contacts