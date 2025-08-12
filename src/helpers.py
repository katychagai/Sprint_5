import faker

def autorization():
    fake = faker.Faker()
    email = fake.email()
    password = fake.password()
    return email, password

