# -*- coding: utf-8 -*-
from model.contact import Contact
import pytest
import random
import string

def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits
    return prefix + ''.join([random.choice(symbols) for i in range(random.randrange(maxlen))])

def random_numbers(prefix, maxlen):
    numbers = string.digits
    return prefix + ''.join([random.choice(numbers) for i in range(random.randrange(maxlen))])

testdata = [Contact(name =random_string("name",10), middlename =random_string("middlename",10),
                    lastname =random_string("lastname",15), nickname =random_string("nickname",10),
                    title =random_string("title",10),company =random_string("company",10),
                    address =random_string("address",50),homephone =random_numbers("",10),
                    mobile=random_numbers("",20), work=random_numbers("",10), fax=random_numbers("",10),
                    email=random_string("email",10), email2=random_string("email2",10),
                    email3=random_string("email3",10),homepage=random_string("hpage",10), bday="5", bmonth="January",
                    byear=random_numbers("",4), address2=random_string("address",10),
                    phone2=random_numbers("",10), notes=random_string("notes",10))
    for i in range(5)]


@pytest.mark.parametrize("contact", testdata, ids=[repr(x) for x in testdata])
def test_add_contact(app, contact):
    old_contacts = app.contact.get_contact_list()
    app.contact.add_contact_form(contact)
    app.contact.submit()
    app.contact.return_home_page()
    assert len(old_contacts) + 1 == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
