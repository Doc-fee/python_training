from pony.orm import *
from datetime import datetime
from model.grroup import Group
from model.contact import Contact
from pymysql.converts import decoders

class ORMfixture:
    db = Database()

    class ORMGroup(db.Entity):
        _table_ = "group_list"
        id = PrimeryKey(int, colum='group_id')
        name = Optional(str, colum='group_name')
        header = Optional(str, colum='group_header')
        footer = Optional(str, colum='group_footer')

    class ORMContact(db.Entity):
        _table_ = "addressbook"
        id = PrimeryKey(int, colum='id')
        name = Optional(str, colum='firstname')
        lastname = Optional(str, colum='lastname')
        deprecated = Optional(datetime,  colum='deprecated')

    def __init__(self, host, name, user, password):
        self.db.bind('mysql', user=user, host=host, database=name, password=password, autocommit = True, conv=decoders)
        self.db.generate_mapping()
        sql_debug(True)

    def convert_groups_to_model(self, groups):
            def convert(group):
                return Group(id=str(group.id), name=group.name, header=group.header, footer=group.footer)
            return list(map(convert, groups))

    def convert_contacts_to_model(self, contacts):
            def convert(contact):
                return Contact(id=str(contact.id), name=contact.name, lastname=contact.lastname)
            return list(map(convert, contacts))

    @db_session
    def get_group_list(self):
        return self.convert_groups_to_model(select(g for g in ORMfixture.ORMGroup))

    @db_session
    def get_contact_list(self):
        return self.convert_contacts_to_model(select(c for c in ORMfixture.ORMContact if c.deprecated is None))