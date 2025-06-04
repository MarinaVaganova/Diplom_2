import pytest
import allure
import requests

from data import *
from helpers import *
from urls import Urls


@allure.feature('Создание пользователя')
class TestUserCreate:
    @allure.title('Проверка успешного создания уникального пользователя')
    def test_create_user_success(self):
        fields = {
            'email': create_random_email(),
            'password': create_random_password(),
            'name': create_random_name()
        }
        response = requests.post(Urls.REGISTER_URL, data=fields)
        assert response.status_code == TestCode.SUCCESS_CODE and TestMessage.MESSAGE_SUCCESS in response.text

    @allure.title('Проверка создания пользователя, который уже зарегистрирован')
    def test_create_duplicate_user_fail(self):
        data = create_new_user()
        response = requests.post(Urls.REGISTER_URL, data = {"email": data[0], "password": data[1], "name": data[2]})
        assert response.status_code == TestCode.FORBIDDEN_CODE and response.json()['message'] == TestMessage.MESSAGE_REGISTER_USER_ALREADY_EXISTS

    @allure.title('Проверка создания пользователя без заполнения одного из обязательных полей')
    @pytest.mark.parametrize('fields',[
        {'email': '', 'password': create_random_password(), 'name': create_random_name()},
        {'email': create_random_email(), 'password': '', 'name': create_random_name()},
        {'email': create_random_email(), 'password': create_random_password(), 'name': ''}
    ])
    def test_create_user_without_required_field_fail(self, fields):
        response = requests.post(Urls.REGISTER_URL, data=fields)
        assert response.status_code == TestCode.FORBIDDEN_CODE and response.json()['message'] == TestMessage.MESSAGE_REGISTER_USER_NO_REQUIRED_FIELDS