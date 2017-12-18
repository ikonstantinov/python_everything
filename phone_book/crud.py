import pickle, os, configparser

crud = {'c': 'Create', 'r': 'Read', 'u': 'Update', 'd': 'Delete'}


def crudFunc():
    for key, items in crud.items():
        print(key, items)

    a = input("Choose one of the options:")
    if not a:
        print("It can't be empty")
        crudFunc()
    return a


def load():
    try:
        with open('phones.txt', 'rb') as f:
            return pickle.load(f)
    except:
        return {}


def add_contact(contact, name, phone):
    if_exists(contact, name)
    contact[name] = phone


def if_exists(contact, name):
    if name in contact:
        raise ValueError


def if_doesnt_exist(contact, name):
    if name not in contact:
        raise ValueError


def update_contact(contact, name, phone):
    if_doesnt_exist(contact, name)
    contact[name] = phone


def delete_contact(contact, name, phone):
    if_doesnt_exist(contact, name)
    del contact[name]


def save(contact):
    try:
        with open('phones.txt', 'wb') as f:
            pickle.dump(contact, f)
    except Exception as e:
        print(e)


def input_name():
    name = input("Contact Name: ")
    return name


def input_phone():
    phone = input("Phone: ")
    return phone


def phone_book(a, contacts):
    if a == 'c':
        name = input_name()
        phone = input_phone()
        add_contact(contacts, name, phone)
        save(contacts)
    elif a == 'r':
        con = load()
        for key, item in con.items():
            print("Name: ", key, " Phone: ", item)
    elif a == 'd':
        name = input_name()
        delete_contact(contacts, name)
        save(contacts)
    elif a == 'u':
        name = input_name()
        phone = input_phone()
        update_contact(contacts, name, phone)
        save(contacts)


def main():
    config = configparser.ConfigParser()
    config.read('settings.txt')
    types = config['DEFAULTS']['filetype']
    print(types)
    f = crudFunc()
    contacts = load()
    phone_book(f, contacts)

if __name__ == '__main__':
    main()






