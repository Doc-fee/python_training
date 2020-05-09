from model.contact import Contact
import random

def test_delete_some_contact(app, db):
    if len(db.get_contact_list()) == 0:
        app.contact.add_contact_form(Contact(name = "Boris", middlename = "Mc", lastname = "Smith", nickname = "Gus", title = "-",company = "IT", address = "Atlantida",
                 homephone = "5556677", mobile='7775558899', work="4182369", fax = "4569632", email="kloun@mail.ru", email2="-", email3="-", homepage="-", bday="5",
                 bmonth="January", byear="2000", address2="world", phone2="7418526", notes="-"))
        app.contact.submit()
        app.contact.return_home_page()
    old_contacts = db.get_contact_list()
    contact = random.choice(old_contacts)
    app.contact.delete_contact_by_id(contact.id)
    new_contacts = db.get_contact_list()
    assert len(old_contacts) - 1 == app.contact.count()
    old_contacts.remove(contact)
    assert old_contacts == new_contacts
    if check_ui:
        assert sorted(new_contacts, key=Contact.id_or_max) == sorted(app.contact.get_contact_list(), key=Contact.id_or_max)