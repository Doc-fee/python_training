# -*- coding: utf-8 -*-
from model.contact import Contact


def test_add_contact(app):
    old_contacts = app.contact.get_contact_list()
    contact =Contact(name = "Anna", middlename = "Mc", lastname = "Smith", nickname = "Ann", title = "-",company = "IT", address = "world",
                      homephone = "5556677", mobile='87459623125', work="4182369", fax = "4569632", email="kloun@mail.ru", email2="-", email3="-", homepage="-", bday="5",
                      bmonth="January", byear="2000", address2="world", phone2="7418526", notes="-")
    app.contact.add_contact_form(contact)
    app.contact.submit()
    app.contact.return_home_page()
    assert len(old_contacts) + 1 == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
