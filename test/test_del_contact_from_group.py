from model.contact import Contact
from model.grroup import Group
import random

def test_del_contact_to_group(app, db, orm):
    # предусловие на наличие группы
    if len(db.get_group_list()) == 0:
        app.group.create(Group(name='test'))

    # предусловие на наличие контакта
    if len(db.get_contact_list()) == 0:
        app.contact.add_contact_form(Contact(name = "Boris", middlename = "Mc", lastname = "Smith", nickname = "Gus", title = "-",company = "IT", address = "Atlantida",
                 homephone = "5556677", mobile='7775558899', work="4182369", fax = "4569632", email="kloun@mail.ru", email2="-", email3="-", homepage="-", bday="5",
                 bmonth="January", byear="2000", address2="world", phone2="7418526", notes="-"))
        app.contact.submit()
        app.contact.return_home_page()

    groups = db.get_group_list()
    group = Group()
    old_contacts_in_group = []

    for gr in groups:
        old_contacts_in_group = orm.get_contacts_in_group(gr)
        if len(old_contacts_in_group) != 0:
            group = gr
            break

    contact_for_del = Contact()

    # предусловие на наличие этого контакта в этой группе
    if len(old_contacts_in_group) == 0:
        group = random.choice(groups)
        contacts = db.get_contact_list()
        contact_for_del = random.choice(contacts)
        app.contact.add_contact_by_id_to_group(contact_for_del.id, group.id)
        old_contacts_in_group = orm.get_contacts_in_group(group)
    else:
        contact_for_del = random.choice(old_contacts_in_group)

    app.contact.del_contact_by_id_from_group(contact_for_del.id, group.id)
    new_contacts_in_group = orm.get_contacts_in_group(group)

    old_contacts_in_group.remove(contact_for_del)
    assert old_contacts_in_group == new_contacts_in_group

