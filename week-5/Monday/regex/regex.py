import re

def filereader():
    with open("regex.txt", "r") as inp:
        text = inp.read()
        v = re.sub(r'\n', '**', text)
        print(v)

def email_address_search():


filereader()
