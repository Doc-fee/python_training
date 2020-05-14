
from model.contact import Contact
from model.grroup import Group
import random

def test_add_contact_to_group(app, db, orm):
    # предусловие наличия контакта
    if len(db.get_contact_list()) == 0:
        app.contact.add_contact_form(Contact(name = "Boris", middlename = "Mc", lastname = "Smith", nickname = "Gus", title = "-",company = "IT", address = "Atlantida",
                 homephone = "5556677", mobile='7775558899', work="4182369", fax = "4569632", email="kloun@mail.ru", email2="-", email3="-", homepage="-", bday="5",
                 bmonth="January", byear="2000", address2="world", phone2="7418526", notes="-"))
        app.contact.submit()
        app.contact.return_home_page()

    # предусловие наличия группы
    if len(db.get_group_list()) == 0:
        app.group.create(Group(name='test'))


    groups = db.get_group_list()
    group = Group()
    contact = Contact()
    contact_not_in = []
    for gr in groups:
        contact_not_in = orm.get_contacts_not_in_group(gr)
        if len(contact_not_in) != 0:
            group = gr
            break

    if len(contact_not_in) == 0:
        app.group.create(Group(name='test'))
        groups_new = db.get_group_list()
        for gr in groups_new:
            contact_not_in = orm.get_contacts_not_in_group(gr)
            if len(contact_not_in) != 0:
                group = gr
                break

    if len(contact_not_in) != 0:
        contact = random.choice(contact_not_in)

    old_contacts_in_group = orm.get_contacts_in_group(group)
    app.contact.add_contact_by_id_to_group(contact.id, group.id)
    new_contacts_in_group = orm.get_contacts_in_group(group)

    old_contacts_in_group.append(contact)
    assert sorted(old_contacts_in_group, key=Contact.id_or_max) == sorted(new_contacts_in_group, key=Contact.id_or_max)

