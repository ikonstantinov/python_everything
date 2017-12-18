import pickle
import os
import configparser


class Controller:
    crud = {'c': 'Create', 'r': 'Read', 'u': 'Update', 'd': 'Delete'}

    def __init__(self):

        f = self.crud_func()
        #config = configparser.ConfigParser()
        #config.read('settings.txt')
        #type = config['DEFAULTS']['filetype']
        #print(type)
        contacts = self.load()
        self.phone_book(f, contacts)

# model - dict с контактами: read, save, create, delete, update (не должно содержать ввод/вывод)
# controller - вызывает методы модели, настройка конфигурации

class Model:
    def phone_book(self, a, contacts):
        if a == 'c':
            name = self.input_name()
            phone = self.input_phone()
            self.add_contact(contacts, name, phone)
            self.save(contacts)
        elif a == 'r':
            con = self.load()
            for key, item in con.items():
                print("Name: ", key, " Phone: ", item)
        elif a == 'd':
            name = self.input_name()
            self.delete_contact(contacts, name)
            self.save(contacts)
        elif a == 'u':
            name = self.input_name()
            phone = self.input_phone()
            self.update_contact(contacts, name, phone)
            self.save(contacts)

    def crud_func(self):
        for key, items in self.crud.items():
            print(key, items)

        a = input("Choose one of the options:")
        if not a:
            print("It can't be empty")
            self.crud_func()
        return a

    def load(self, filename='phones.txt'):
        try:
            with open(filename, 'rb') as f:
                return pickle.load(f)
        except:
            return {}

    def add_contact(self, contact, name, phone):
        self.if_exists(contact, name)
        contact[name] = phone

    def if_exists(self, contact, name):
        if name in contact:
            raise ValueError

    def if_doesnt_exist(self, contact, name):
        if name not in contact:
            raise ValueError

    def update_contact(self, contact, name, phone):
        self.if_doesnt_exist(contact, name)
        contact[name] = phone

    def delete_contact(self,contact, name):
        self.if_doesnt_exist(contact, name)
        del contact[name]

    def save(self,contact):
        try:
            with open('phones.txt', 'wb') as f:
                pickle.dump(contact, f)
        except Exception as e:
            print(e)

    def input_name(self):
        name = input("Contact Name: ")
        return name

    def input_phone(self):
        phone = input("Phone: ")
        return phone



