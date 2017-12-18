import pickle, os

CONTACTS_DATA_FILE = 'contacts.txt'

crud = {'c': 'Create', 'r': 'Read', 'u': 'Update', 'd': 'Delete'}
#contacts = {'Peter': 12345, 'Sarah': 2346, 'Ivan': 123467, 'Karen': 3091}


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
        with open('phones.txt', 'r') as f:
            return pickle.load(f)
    except:
        return {}


def save():
    try:
        with open('phones.txt', 'w') as f:
            pickle.dumps(f)
    except Exception as e:
        print(e)





#    with open('phones.txt', 'w') as f:
 #       contacts = pickle.dumb(contacts, f)

def add_item(dictionary, name, phone):
    try:
        with open(CONTACTS_DATA_FILE, 'w') as cf:
            return pickle.dumps(CONTACTS_DATA_FILE, cf)
    except FileNotFoundError:
        pass
    return []
    #dictionary[name] = phone


def update_item(dictionary, name, phone):
    dictionary[name] = phone


def delete_item(dictn=None, name=None):
    del dictn[name]


def read_contacts():
    try:
        with open(CONTACTS_DATA_FILE, 'rb') as cf:
            for key in cf.read():
                print("Name: ", pickle.load(key), " Phone: ")
            return pickle.load(cf)

    except FileNotFoundError:
        pass
    return []


def input_name():
    name = input("Contact Name: ")
    return name


def input_phone():
    phone = input("Phone: ")
    if not phone:
        print("Phone Can't be empty!")
        input_phone()
    else:
        return phone


def is_exist(dictionary, name):
    if name in dictionary:
        return True
    else:
        return False


def phone_book(a):
    if a == 'c':
        name = input_name()
        if not name:
            print("Name can't be empty")
            input_name()
        else:
            if is_exist(contacts, name) is False:
                phone = input_phone()
                pickle.dumps(add_item(contacts,name,phone))
                main()
            else:
                print('This contact is already present, want to update it?')
                main()
    elif a == 'u':
        name = input_name()
        if is_exist(contacts, name) is True:
            phone = input_phone()
            update_item(contacts, name, phone)
            main()
        else:
            print("There is no such contact!")
            main()
    elif a == 'r':
        read_contacts()
        main()

    elif a == 'd':
        name = input("Contact Name: ")
        if is_exist(contacts, name):
            delete_item(contacts, name)
            main()
        else:
            print("There is no such contact!")
            main()


def main():
    f = crudFunc()
    contacts = load()
    phone_book(f)

if __name__ == '__main__':
    main()






