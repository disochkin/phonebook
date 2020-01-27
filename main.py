favorite_status = ["Нет","Да"]


class Contact:
    def __init__(self, firstname, lastname, phonenumber, favorite=False, **kwargs):
        self.firstname = firstname
        self.lastname = lastname
        self.phonenumber = phonenumber
        self.favorite = favorite
        self.addinfo = kwargs

    def __str__(self):
        result = f'Имя: {self.firstname}\nФамилия: {self.lastname}\nТелефон: {self.phonenumber}\n' \
                 f'В избранных: {favorite_status[self.favorite]}\n'
        if self.addinfo:
            result = result + f'Дополнительная информация:\n'
            for category, content in self.addinfo.items():
                result = result + f'\t{category}: {content}\n'
        return result

def get_user_input(query):
    user_input = input(query).lower()
    return user_input

def create_contact():
    additional_info = {}
    first_name = get_user_input("Введите имя:")
    last_name = get_user_input("Введите фамилию:")
    telephone_number = get_user_input("Введите номер телефона:")
    favorite_status = bool(get_user_input("Избранный контакт (0-нет,1-да):"))
    while True:
        if get_user_input("Добавить допополнительную информацию? 0-нет,1-да") == "1":
            key = get_user_input("Введите название поля доп.информации:")
            value = get_user_input("Введите значение поля доп.информации:")
            additional_info.update({key:value})
        else:
            break
    print(additional_info)
    contact = Contact(first_name, last_name, telephone_number, favorite_status, **additional_info)
    return contact

def remove_contact(phonebook):
    number_of_contact_for_remove = get_user_input("Введите номер удаляемого контакта:")
    phonebook.removecontact(number_of_contact_for_remove)

def findbyfirstname(phonebook):
    firstname = get_user_input("Введите имя контакта:")
    phonebook.findbyfirstname(firstname)

def findbylastname(phonebook):
    lastname = get_user_input("Введите фамилию контакта:")
    phonebook.findbylastname(lastname)

class PhoneBook:
    def __init__(self, name):
        self.name = name
        self.contacts = []

    def addcontact(self, contact):
        self.contacts.append(contact)

    def getallcontats(self):
        for contact in self.contacts:
            print(contact)

    def getfavorites(self):
        for contact in self.contacts:
            if contact.favorite:
                print(contact)

    def removecontact(self,phonenumber):
        for contact in self.contacts:
            if contact.phonenumber == phonenumber:
                self.contacts.remove(contact)
                print('Контакт удален')


    def findbyfirstname(self,firstname):
        for contact in self.contacts:
            if contact.firstname.lower() == firstname.lower():
                print(contact)

    def findbylastname(self,lastname):
        for contact in self.contacts:
            if contact.lastname.lower() == lastname.lower():
                print(contact)

def main():

    while True:
        user_input = get_user_input("Введите команду:\n\
    1-Вывод контактов из телефонной книги\n\
    2-Добавление нового контакта\n\
    3-Удаление контакта по номеру телефона\n\
    4-Поиск всех избранных номеров\n\
    5-Поиск контакта по имени\n\
    6-Поиск контакта по фамилии\n")
        if user_input == '1':
            pb1.getallcontats()
        elif user_input == '2':
            pb1.addcontact(create_contact())
        elif user_input == '3':
            remove_contact(pb1)
        elif user_input == '4':
            pb1.getfavorites()
        elif user_input == '5':
            findbyfirstname(pb1)
        elif user_input == '6':
            findbylastname(pb1)




pb1 = PhoneBook("Phonebook#1")
user1 = Contact('Jhon', 'Smith', '+71234567809', telegram='@jhony', email='jhony@smith.com')
user2 = Contact('Bob', 'Tyler', '+71234567809', favorite=True)
user3 = Contact('Bill', 'Gilbert', '+71234567809', favorite=True)

pb1.addcontact(user1)
pb1.addcontact(user2)
pb1.addcontact(user3)

main()

