from model.contact import Contact
import random

def test_edit_some_contact(app, db, check_ui):
    if len(db.get_contact_list()) == 0:
        app.contact.add_contact_form(Contact(name = "Anna", middlename = "Mc", lastname = "Smith", nickname = "Ann", title = "-",company = "IT", address = "world",
                 homephone = "5556677", mobile='87459623125', work="4182369", fax = "4569632", email="kloun@mail.ru", email2="-", email3="-", homepage="-", bday="5",
                 bmonth="January", byear="2000", address2="world", phone2="7418526", notes="-"))
        app.contact.submit()
        app.contact.return_home_page()
    old_contacts = db.get_contact_list()
    contact = random.choice(old_contacts)
    contactchange = Contact(name = "Boris", nickname = "Gus", lastname = "Lee")
    contactchange.id = contact.id
    app.contact.edit_contact_by_id(contact.id, contactchange)
#    assert len(old_contacts) == app.contact.count()
    new_contacts = db.get_contact_list()
    index = 0
    for item in old_contacts:
        if item.id == contact.id:
            old_contacts[index] = contactchange
        index += 1
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
    if check_ui:
        assert sorted(new_groups, key=Group.id_or_max) == sorted(app.group.get_group_list(), key=Group.id_or_max)
