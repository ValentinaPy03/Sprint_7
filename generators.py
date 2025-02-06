from faker import Faker

fake = Faker()

def generate_courier_body():
    return {
        "login": fake.word() ,
        "password": fake.random_int(min=1000, max=9999),
        "firstName": fake.first_name()
    }

def generate_courier_body_without_login():
    return {
        "password": fake.random_int(min=1000, max=9999),
        "firstName": fake.first_name()
    }

def generate_courier_body_with_same_login(login):
    return {
        "login": login,
        "password": fake.random_int(min=1000, max=9999),
        "firstName": fake.first_name()
    }

def generate_incorrect_password():
    return fake.word()

def generate_incorrect_login():
    return fake.word()

def generate_order_body():
    return {
        "firstName": fake.first_name(),
        "lastName": fake.last_name(),
        "address": fake.address(),
        "metroStation": fake.random_int(1, 10),
        "phone": fake.phone_number(),
        "rentTime": fake.random_int(1, 15),
        "deliveryDate": fake.date_between('today', '+30d').isoformat(),
        "comment": " ".join(fake.words(3)),
        "color": [
            'BLACK'
        ]
    }

