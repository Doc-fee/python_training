from model.contact import Contact
import re

class ContactHelper:

    def __init__(self, app):
        self.app = app

    def return_home_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("home").click()

    def delete_first_contact(self):
        self.delete_contact_by_index(0)

    def delete_contact_by_index(self, index):
        wd = self.app.wd
        # select contact by index
        wd.find_elements_by_name("selected[]")[index].click()
        # submit delete
        wd.find_element_by_xpath("//input[@value='Delete']").click()
        # close dialog module
        wd.switch_to_alert().accept()
        wd.find_element_by_xpath("//div[@id='content']/div[@class='msgbox']")
        self.return_home_page()
        self.contact_cache = None

    def edit_first_contact(self, contact):
        self.edit_contact_by_index(0, contact)
    #Доработала
    def edit_contact_by_index(self, index, contact):
        wd = self.app.wd
        # select contact by index
        #wd.find_elements_by_name("selected[]")[index].click()
        self.click_edit_by_index(index)
        #wd.find_element_by_xpath("//img[@alt='Edit']")[index].click()
        # fill forms
        self.fill_contact(contact)
        # update info
        wd.find_element_by_name("update").click()
        self.return_home_page()
        self.contact_cache = None

    def click_edit_by_index(self, index):
        wd = self.app.wd
        self.app.open_home_page()
        element = wd.find_elements_by_name("entry")[index]
        pencil = element.find_elements_by_tag_name("td")[7]
        pencil.find_element_by_tag_name("a").click()

    def click_details_by_index(self, index):
        wd = self.app.wd
        self.app.open_home_page()
        element = wd.find_elements_by_name("entry")[index]
        person = element.find_elements_by_tag_name("td")[6]
        person.find_element_by_tag_name("a").click()

    def submit(self):
        wd = self.app.wd
        wd.find_element_by_xpath("(//input[@name='submit'])[2]").click()

    def add_contact_form(self,  contact):
        wd = self.app.wd
        # add new contact
        wd.find_element_by_link_text("add new").click()
        # fill forms
        self.fill_contact(contact)
        self.contact_cache = None

    def fill_contact(self, contact):
        wd = self.app.wd
        # add first name
        self.change_field_value("firstname", contact.name)
        # add middle name
        self.change_field_value("middlename", contact.middlename )
        # add last name
        self.change_field_value("lastname", contact.lastname)
        # add nickname
        self.change_field_value("nickname", contact.nickname)
        # add title
        self.change_field_value("title", contact.title)
        # add company
        self.change_field_value("company", contact.company)
        # add address
        self.change_field_value("address", contact.address)
        # add telephone
        self.change_field_value("home", contact.homephone)

        self.change_field_value("mobile", contact.mobile)
        self.change_field_value("work", contact.work)
        self.change_field_value("fax", contact.fax)
        # add email
        self.change_field_value("email", contact.email)
        self.change_field_value("email2", contact.email2)
        self.change_field_value("email3", contact.email3)
        self.change_field_value("homepage", contact.homepage)
         # add b-day
        wd.find_element_by_name("bday").click()
        #Select(driver.find_element_by_name("bday")).select_by_visible_text(contact.bday)
        wd.find_element_by_xpath("//option[@value='"+contact.bday+"']").click()
        wd.find_element_by_name("bmonth").click()
        #Select(driver.find_element_by_name("bmonth")).select_by_visible_text(contact.bmonth)
        wd.find_element_by_xpath("//option[@value='"+contact.bmonth+"']").click()
        self.change_field_value("byear", contact.byear)
        # add address 2
        self.change_field_value("address2", contact.address2)
        # add home telephone
        self.change_field_value("phone2", contact.phone2)
        # add notes
        self.change_field_value("notes", contact.notes)

    def change_field_value(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)

    def count(self):
        wd = self.app.wd
        self.app.open_home_page()
        return len(wd.find_elements_by_name("selected[]"))

    contact_cache = None

    def get_contact_list(self):
        if self.contact_cache is None:
            wd = self.app.wd
            self.app.open_home_page()
            self.contact_cache = []
            elementsTd = []
            for element in wd.find_elements_by_css_selector("tr[name=entry]"):
                elementsTd = element.find_elements_by_css_selector("td")
                lastName = elementsTd[1].text
                firstName = elementsTd[2].text
                id = element.find_element_by_name("selected[]").get_attribute("value")
                all_phones = elementsTd[5].text
                all_emails = elementsTd[4].text
                address = elementsTd[3].text
                self.contact_cache.append(Contact(name=firstName, id=id, lastname=lastName,
                                                  all_phones_from_home_page=all_phones,
                                                  all_emails_from_home_page=all_emails,
                                                  address=address))
        return list(self.contact_cache)

    def get_contact_info_from_edit_page(self, index):
        wd = self.app.wd
        self.click_edit_by_index(index)
        firstname = wd.find_element_by_name("firstname").get_attribute('value')
        lastname = wd.find_element_by_name("lastname").get_attribute('value')
        id = wd.find_element_by_name("id").get_attribute('value')
        homephone = wd.find_element_by_name("home").get_attribute('value')
        work = wd.find_element_by_name("work").get_attribute('value')
        mobile = wd.find_element_by_name("mobile").get_attribute('value')
        phone2 = wd.find_element_by_name("phone2").get_attribute('value')
        email = wd.find_element_by_name("email").get_attribute('value')
        email2 = wd.find_element_by_name("email2").get_attribute('value')
        email3 = wd.find_element_by_name("email3").get_attribute('value')
        address = wd.find_element_by_name("address").get_attribute('value')
        return Contact(name=firstname, lastname=lastname, id=id,
                       homephone=homephone, mobile=mobile, work=work, phone2=phone2,
                       email=email, email2=email2, email3=email3, address=address)

    def get_contact_from_view_page(self, index):
        wd = self.app.wd
        self.click_details_by_index(index)
        text = wd.find_element_by_id("content").text
        homephone = re.search("H: (.*)", text).group(1)
        work = re.search("W: (.*)", text).group(1)
        mobile = re.search("M: (.*)", text).group(1)
        phone2 = re.search("P: (.*)", text).group(1)
        return Contact(homephone=homephone, mobile=mobile, work=work, phone2=phone2)

    def delete_contact_by_id(self, id):
        wd = self.app.wd
        # select contact by id
        wd.find_element_by_css_selector("input[value='%s']" % id).click()
        # submit delete
        wd.find_element_by_xpath("//input[@value='Delete']").click()
        # close dialog module
        wd.switch_to_alert().accept()
        wd.find_element_by_xpath("//div[@id='content']/div[@class='msgbox']")
        self.return_home_page()
        self.contact_cache = None

    def edit_contact_by_id(self, id, contact):
        wd = self.app.wd
        # select contact by index
        #wd.find_elements_by_name("selected[]")[index].click()
        self.click_edit_by_id(id)
        #wd.find_element_by_xpath("//img[@alt='Edit']")[index].click()
        # fill forms
        self.fill_contact(contact)
        # update info
        wd.find_element_by_name("update").click()
        self.return_home_page()
        self.contact_cache = None

    def click_edit_by_id(self, id):
        wd = self.app.wd
        self.app.open_home_page()
        # element = wd.find_elements_by_name("entry")[index]
        # pencil = element.find_elements_by_tag_name("td")[7]
        # pencil.find_element_by_tag_name("a").click()
        wd.find_element_by_css_selector("a[href='edit.php?id=%s']" % id).click()


    def add_contact_by_id_to_group(self, contact_id, group_id):
        wd = self.app.wd
        self.app.open_home_page()
        # select contact by id
        wd.find_element_by_css_selector("input[value='%s']" % contact_id).click()
        wd.find_element_by_xpath("//select[@name='to_group']/option[@value='"+group_id+"']").click()
        wd.find_element_by_xpath("(//input[@name='add'])").click()
        self.return_home_page()






