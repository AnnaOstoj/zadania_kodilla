from faker import Faker


class BaseContact:
    def __init__(self, first_name, last_name, phone, email):
        self.first_name = first_name
        self.last_name = last_name
        self.phone = phone
        self.email = email

    def __str__(self):
        return f"{self.first_name}, {self.last_name}, {self.phone}, {self.email}"

    def contact(self):
        return print(
            f"Wybieram numer {self.phone} i dzwonię do"  
            + f"{self.first_name} {self.last_name}")

    @ property
    def name_length(self):
        return len(self.first_name + self.last_name)


class BusinessContact(BaseContact):
    def __init__(self, position, company, company_phone, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.position = position
        self.company = company
        self.company_phone = company_phone

    def __str__(self):
        return f"{self.position},  {self.company}, {self.company_phone}"

    def contact(self):
        return print(
            f"Wybieram numer {self.company_phone} i "
            + f"dzwonię do {self.first_name} {self.last_name}")

    @ property
    def name_length(self):
        return len(self.first_name + self.last_name)


fake = Faker("fr_FR")


def create_contacts(card_type, amount):
    card_list = []
    for i in range(amount):
        if card_type == "BaseContact":
            card_list.append(BaseContact(
                first_name=fake.first_name(),
                last_name=fake.last_name(), phone=fake.phone_number(),
                email=fake.free_email()))
        else:
            card_list.append(BusinessContact(
                first_name=fake.first_name(),
                last_name=fake.last_name(), phone=fake.phone_number(),
                email=fake.free_email(), position=fake.job(),
                company=fake.company(),
                company_phone=fake.phone_number()))
    return card_list


people = create_contacts("BaseContact", 10)

for item in people:
    item.contact()
