from model.contact import Contact

def test_edit_first_contact(app):
    app.contact.edit_first_contact(Contact(name = "Boris", middlename = "Mc", lastname = "Smith", nickname = "Gus", title = "-",company = "IT", address = "Atlantida",
                 homephone = "5556677", mobile='7775558899', work="4182369", fax = "4569632", email="kloun@mail.ru", email2="-", email3="-", homepage="-", bday="5",
                 bmonth="January", byear="2000", address2="world", phone2="7418526", notes="-"))
