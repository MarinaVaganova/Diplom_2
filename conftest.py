import pytest
import requests

from data import *
from helpers import *
from urls import Urls


@pytest.fixture(scope='function')
def get_token():
    data = create_new_user()
    response = requests.post(Urls.LOGIN_URL, data = {"email": data[0], "password": data[1], "name": data[2]})
    token = response.json().get('accessToken')
    yield token
    requests.delete(Urls.USER_URL, headers={"Authorization": f'{token}'})

@pytest.fixture(scope='function')
def get_ingredients():
    response = requests.get(Urls.INGREDIENTS)
    if response.status_code == TestCode.SUCCESS_CODE:
        return response.json()['data']
    else:
        raise Exception(f'Не удалось получить ингредиенты: {response.text}')