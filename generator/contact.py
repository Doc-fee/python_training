from model.contact import Contact
import random
import string
import os.path
import json
import getopt
import sys

try:
    opts, args = getopt.getopt(sys.argv[1:], 'n:f:', ['number of contacts', 'file'])
except getopt.GetoptError as err:
    getopt.usage()
    sys.exit(2)
n = 5
f = 'data/contacts.json'

for o, a in opts:
    if o == '-n':
        n = int(a)
    elif o == '-f':
        f = a

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
    for i in range(n)]

file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", f)

with open(file, "w") as out:
    out.write(json.dump(testdata, defalt=lambda x: x.__dict__, indent = 2))