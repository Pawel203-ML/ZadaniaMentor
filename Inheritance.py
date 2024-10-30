from faker import Faker
fake = Faker()

class AddressBook:
    def __init__(self, name, surname, job, company, mail):
        self.name = name
        self.surname = surname
        self.job = job
        self.company = company
        self.mail = mail

class BaseContact(AddressBook):
    def __init__(self,priv_phone, *args, **kwargs):
        super().__init__(*args,**kwargs)
        self.priv_phone = priv_phone
        self._label_length = 0

    def contact(self):
        return f'Wybieram numer {self.priv_phone} i dzwonie do {self.name} {self.surname}'


class BusinessContact(AddressBook):
    def __init__(self,business_phone, *args, **kwargs):
        super().__init__(*args,**kwargs)
        self.business_phone = business_phone

    def contact(self):
        return f'Wybieram numer {self.business_phone} i dzwonie do {self.name} {self.surname}'


BaseContactList = []
BusinessContactList =[]