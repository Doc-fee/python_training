from model.contact import Contact

class ContactHelper:

    def __init__(self, app):
        self.app = app

    def return_home_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("home").click()

    def delete_first_contact(self):
        wd = self.app.wd
        # select first contact
        wd.find_element_by_name("selected[]").click()
        # submit delete
        wd.find_element_by_xpath("//input[@value='Delete']").click()
        # close dialog module
        wd.switch_to_alert().accept()
        wd.find_element_by_xpath("//div[@id='content']/div[@class='msgbox']")
        self.return_home_page()
        self.contact_cache = None

    def edit_first_contact(self, contact):
        wd = self.app.wd
        # click Edit
        wd.find_element_by_xpath("//img[@alt='Edit']").click()
        # fill forms
        self.fill_contact(contact)
        # update info
        wd.find_element_by_name("update").click()
        self.return_home_page()
        self.contact_cache = None

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
                self.contact_cache.append(Contact(name=firstName, id=id, lastname=lastName))
        return list(self.contact_cache)