import requests

from faker import Faker
from urls import Urls
from data import TestCode
from random import sample


fake = Faker()
fakeRU = Faker(locale='ru_RU')

def create_random_email():
    email = f'marina_20_{fake.email()}'
    return email

def create_random_password():
    password = fake.password()
    return password

def create_random_name():
    name = fakeRU.first_name()
    return name

def create_new_user():
    user_data = []
    email = create_random_email()
    password = create_random_password()
    name = create_random_name()

    payload = {
        'email': email,
        'password': password,
        'name': name
    }
    response = requests.post(Urls.REGISTER_URL, data=payload)
    if response.status_code == TestCode.SUCCESS_CODE:
        user_data.append(email)
        user_data.append(password)
        user_data.append(name)
    else:
        raise Exception(f'Не удалось зарегистрировать пользователя: {response.text}')
    return user_data

def create_order_data(get_ingredients, count=3):
    return sample([ing['_id'] for ing in get_ingredients], count)