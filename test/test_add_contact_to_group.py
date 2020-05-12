
from model.contact import Contact
from model.grroup import Group
import random

def test_add_contact_to_group(app, db, orm):
    if len(db.get_contact_list()) == 0:
        app.contact.add_contact_form(Contact(name = "Boris", middlename = "Mc", lastname = "Smith", nickname = "Gus", title = "-",company = "IT", address = "Atlantida",
                 homephone = "5556677", mobile='7775558899', work="4182369", fax = "4569632", email="kloun@mail.ru", email2="-", email3="-", homepage="-", bday="5",
                 bmonth="January", byear="2000", address2="world", phone2="7418526", notes="-"))
        app.contact.submit()
        app.contact.return_home_page()
    if len(db.get_group_list()) == 0:
        app.group.create(Group(name='test'))

    groups = db.get_group_list()
    contacts = db.get_contact_list()
    contact = random.choice(contacts)
    group = random.choice(groups)

    old_contacts_in_group = orm.get_contacts_in_group(group)
    app.contact.add_contact_by_id_to_group(contact.id, group.id)
    new_contacts_in_group = orm.get_contacts_in_group(group)

    old_contacts_in_group.append(contact)
    assert sorted(old_contacts_in_group, key=Contact.id_or_max) == sorted(new_contacts_in_group, key=Contact.id_or_max)

