import pickle

FILENAME = 'contacts.dat'

def load_contacts():
    try:
        with open(FILENAME, 'r') as f:
            return pickle.load(f)
    except IOError, EOFError:
        return {}
        
def save_contacts():
    with open(FILENAME, 'w') as f:
        pickle.dump(contacts, f)

def create_contact(name, phone):
    if name in contacts:
          raise ValueError("Name exists")
    contacts[name] = phone
    
def find_contact(name):
    try:
        return contacts[name]
    except KeyError:
        raise ValueError("Name doesn't exist")
        
def ask_name():
    return raw_input('name?')
        
def ask_create_contacts():
    name = ask_name()
    phone = raw_input('phone?')
    try:
         create_contact(name, phone)
    except ValueError as e:
         print e

def ask_find_contact():
    name = name = ask_name()
    try:
        print name, find_contact(name)
    except ValueError as e:
        print e

controller = {
    'c': ask_create_contacts,
    'f': ask_find_contact,
}

def default():
    print "Invalid action"
    
    
contacts = load_contacts()
while True:
    action = raw_input("Action?")
    if action in "Qq":
        break
    controller.get(action.lower(), default)()
    
save_contacts()
