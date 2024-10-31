from faker import Faker
fake = Faker()

class AddressBook:
    def __init__(self, name, surname, job, company, mail):
        self.name = name
        self.surname = surname
        self.job = job
        self.company = company
        self.mail = mail

    def __str__(self):
        return f'{self.name} {self.surname}'

class BaseContact(AddressBook):
    def __init__(self,priv_phone, *args, **kwargs):
        super().__init__(*args,**kwargs)
        self.priv_phone = priv_phone
        self._label_length = 0

    def contact(self):
        return f'Wybieram numer {self.priv_phone} i dzwonie do {self.name} {self.surname}'
    
    def __str__(self):
        return f'{self.name} {self.surname} {self.priv_phone} {self.mail}'

    @property
    def label_length(self):
        return f' Dlugosz imeinia i nazwiska to: {self._label_length}'
    @label_length.setter
    def label_length(self, value):
        self._label_length = value


class BusinessContact(AddressBook):
    def __init__(self,business_phone, *args, **kwargs):
        super().__init__(*args,**kwargs)
        self.business_phone = business_phone
        self._label_length = 0

    def contact(self):
        return f'Wybieram numer {self.business_phone} i dzwonie do {self.name} {self.surname}'
    
    def __str__(self):
        return f'{self.name} {self.surname} {self.business_phone} {self.company}'
    
    @property
    def label_length(self):
        return f' Dlugosz imeinia i nazwiska to: {self._label_length}'
    @label_length.setter
    def label_length(self, value):
        self._label_length = value


def SearchingNames():
    #przeszukuje listy i tworzy odpowiednie frazy
    print('--BaseContact--')
    for person in BaseContactList:
        print(person)
        value = len(person.name) 
        value += len(person.surname) + 1
        person.label_length = value
        print(person.label_length)
        print('  ', person.contact())
    print('\n')
    print('--BusinessContact--')
    for person in BusinessContactList:
        print(person)
        value = len(person.name)
        value += len(person.surname) + 1
        person.label_length = value
        print(person.label_length)
        print('  ', person.contact())
        
        


BaseContactList = []
BusinessContactList =[]

#dodawanie wartosci do list
random_number = fake.random_int(1,5)
for i in range(random_number):
    BaseContactList.append(BaseContact(name= fake.name(), surname= fake.last_name(), job= fake.job(), company= fake.company(), mail= fake.email(), priv_phone= fake.phone_number()))
random_number = fake.random_int(1,6)
for i in range(random_number):
    BusinessContactList.append(BusinessContact(name= fake.name(), surname= fake.last_name(), job= fake.job(), company= fake.company(), mail= fake.email(), business_phone= fake.phone_number()))

SearchingNames()