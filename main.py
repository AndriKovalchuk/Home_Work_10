from collections import UserDict


class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)


class Name(Field):
    pass


class Phone(Field):
    def __init__(self, value):
        super().__init__(value)
        self.phone_valid(value)

    def phone_valid(self, phone):
        if len(phone) != 10 or not phone.isdigit():
            raise ValueError('Invalid phone number.')
        return True


class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []

    def add_phone(self, phone):
        try:
            p = Phone(phone)    # created p which is an instance of class Phone
            if p.phone_valid(phone):
                self.phones.append(p)
        except ValueError as e:
            print(e)

    def edit_phone(self, old_phone, new_phone):
        phone_found = False
        for p in self.phones:
            if p.value == old_phone:
                p.value = new_phone
                phone_found = True
                break
        if not phone_found:
            raise ValueError('Phone was not found.')

    def find_phone(self, phone):
        for p in self.phones:
            if p.value == phone:
                return p
        return None

    def remove_phone(self, phone):
        for p in self.phones:
            if p.value == phone:
                self.phones.remove(p)

    def __str__(self):
        return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}"


class AddressBook(UserDict):
    def add_record(self, contact):
        self.data.update({contact.name.value: contact})

    def find(self, name):
        if name in self.data:
            return self.data[name]
        else:
            print('Phone was not found.')

    def delete(self, name):
        try:
            if name in self.data:
                self.data.pop(name)
            else:
                raise KeyError
        except KeyError:
            print(f'"{name}" is not in the address book.')
