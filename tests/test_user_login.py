import pytest
import allure
import requests

from helpers import *
from urls import Urls
from data import *


@allure.feature('Логин пользователя')
class TestUserLogin:
    @allure.title('Проверка авторизации существующего пользователя')
    def test_login_user_success(self):
        data = create_new_user()
        response = requests.post(Urls.LOGIN_URL, data = {"email": data[0], "password": data[1]})
        assert response.status_code == TestCode.SUCCESS_CODE and TestMessage.MESSAGE_SUCCESS in response.text

    @allure.title('Проверка авторизации в неверным логином и паролем')
    @pytest.mark.parametrize('fields',[
        lambda user_data: {'email': user_data[0], 'password': user_data[2]},
        lambda user_data: {'email': user_data[2], 'password': user_data[1]}
    ])
    def test_login_user_invalid_email_or_password_fail(self, fields):
        data = create_new_user()
        field = fields(data)
        response = requests.post(Urls.LOGIN_URL, data=field)
        assert response.status_code == TestCode.UNAUTHORIZED_CODE and response.json()['message'] == TestMessage.MESSAGE_AUTH_LOGIN_UNAUTHORIZED