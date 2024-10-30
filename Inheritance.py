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
        return f'{self.priv_phone} {self.mail}'


class BusinessContact(AddressBook):
    def __init__(self,business_phone, *args, **kwargs):
        super().__init__(*args,**kwargs)
        self.business_phone = business_phone

    def contact(self):
        return f'Wybieram numer {self.business_phone} i dzwonie do {self.name} {self.surname}'
    
    def __str__(self):
        return f'{self.business_phone} {self.company}'


BaseContactList = []
BusinessContactList =[]

#dodawanie wartosci do list
for i in range(5):
    BaseContactList.append(BaseContact(name= fake.name(), surname= fake.last_name(), job= fake.job(), company= fake.company(), mail= fake.email(), priv_phone= fake.phone_number()))
    BusinessContactList.append(BusinessContact(name= fake.name(), surname= fake.last_name(), job= fake.job(), company= fake.company(), mail= fake.email(), business_phone= fake.phone_number()))

