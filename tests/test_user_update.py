import pytest
import allure
import requests

from helpers import *
from data import *


@allure.feature('Изменение данных пользователя')
class TestUserUpdate:
    @allure.title('Проверка изменения данных пользователя с авторизацией')
    @pytest.mark.parametrize('field, value', [
        ('email', create_random_email()),
        ('password', create_random_password()),
        ('name', create_random_name())
    ])
    def test_update_user_with_auth_success(self, get_token, field, value):
        token = get_token
        payload = {field: value}
        headers = {"Content-type": "application/json", "Authorization": f'{token}'}
        response = requests.patch(Urls.USER_URL, headers=headers, json=payload)
        assert response.status_code == TestCode.SUCCESS_CODE and TestMessage.MESSAGE_SUCCESS in response.text

    @allure.title('Проверка изменения данных пользователя без авторизации')
    def test_update_user_without_auth_fail(self):
        payload = {'email': create_random_email(), 'password': create_random_password()}
        headers = {"Content-type": "application/json"}
        response = requests.patch(Urls.USER_URL, headers=headers, json=payload)
        assert response.status_code == TestCode.UNAUTHORIZED_CODE and response.json()['message'] == TestMessage.MESSAGE_CHANGE_DATA_UNAUTHORIZED