from model.contact import Contact
import re

def test_contacts_home_page(app,db):
    contact_from_home_page = app.contact.get_contact_list()
    contact_from_db = db.get_means_of_communication()
    new_contact_from_db = list(map(merge_phones_like_on_home_page, contact_from_db))
    new_contact_from_dbe = list(map(merge_emails_like_on_home_page, new_contact_from_db))

    sort_contact_from_home_page = sorted(contact_from_home_page, key=Contact.id_or_max)
    sort_contact_from_db = sorted(new_contact_from_dbe, key=Contact.id_or_max)

    #name
    for number in range(len(sort_contact_from_db)):
        assert sort_contact_from_db[number].name == sort_contact_from_home_page[number].name

    #lastname
    for number in range(len(sort_contact_from_db)):
        assert sort_contact_from_db[number].lastname == sort_contact_from_home_page[number].lastname

    # phones
    for number in range(len(sort_contact_from_db)):
        assert sort_contact_from_db[number].all_phones_from_home_page == sort_contact_from_home_page[number].all_phones_from_home_page

    # address
    for number in range(len(sort_contact_from_db)):
        assert sort_contact_from_db[number].address == sort_contact_from_home_page[number].address

    # emails
    for num in range(len(sort_contact_from_db)):
        assert sort_contact_from_db[num].all_emails_from_home_page == sort_contact_from_home_page[num].all_emails_from_home_page


# def test_phones_on_contact_view_page(app):
#     contact_from_view_page = app.contact.get_contact_from_view_page(0)
#     contact_from_edit_page = app.contact.get_contact_info_from_edit_page(0)
#     assert contact_from_view_page.homephone == contact_from_edit_page.homephone
#     assert contact_from_view_page.mobile == contact_from_edit_page.mobile
#     assert contact_from_view_page.work == contact_from_edit_page.work
#     assert contact_from_view_page.phone2 == contact_from_edit_page.phone2

def clear_phones(s):
        return re.sub("[() -]","", s)

def merge_phones_like_on_home_page(contact):
    all_phones = "\n".join(filter(lambda x: x != "",
                            map(lambda x: clear_phones(x), [contact.homephone, contact.mobile, contact.work, contact.phone2])))
    contact.all_phones_from_home_page = all_phones
    return contact

def clear_emails(a):
    return re.sub("[ ]", "", a)

def merge_emails_like_on_home_page(contact):
    all_emails = "\n".join(filter(lambda x: x != "",
                            map(lambda x: clear_emails(x), [contact.email, contact.email2, contact.email3])))
    contact.all_emails_from_home_page = all_emails
    return contact