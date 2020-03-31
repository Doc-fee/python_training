# -*- coding: utf-8 -*-
import pytest
from model.contact import Contact
from fixture.Aplication_contact import Aplication_co


@pytest.fixture
def app(request):
    fixture = Aplication_co()
    request.addfinalizer(fixture.destroy)
    return fixture

def test_add_contact(app):
    app.session.login(username="admin", password="secret")
    app.contact.fill_contact_form(Contact(name = "Anna", middlename = "Mc", lastname = "Smith", nickname = "Ann", title = "-",company = "IT", address = "world",
                 homephone = "5556677", mobile='87459623125', work="4182369", fax = "4569632", email="kloun@mail.ru", email2="-", email3="-", homepage="-", bday="5",
                 bmonth="January", byear="2000", address2="world", phone2="7418526", notes="-"))
    app.contact.submit()
    app.contact.return_home_page()
    app.session.logout()