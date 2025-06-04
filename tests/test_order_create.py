import pytest
import allure
import requests

from helpers import *
from data import *


@allure.feature('Создание заказа')
class TestOrderCreate:
    @allure.title('Проверка создания заказа с авторизацией')
    def test_order_create_with_auth_success(self, get_token, get_ingredients):
        order_data = {"ingredients": create_order_data(get_ingredients)}
        token = get_token
        headers = {"Content-type": "application/json", "Authorization": f'{token}'}
        response = requests.post(Urls.ORDERS_URL, headers=headers, json=order_data)
        assert response.status_code == TestCode.SUCCESS_CODE and TestMessage.MESSAGE_SUCCESS in response.text

    @allure.title('Проверка создания заказа без авторизации')
    def test_order_create_without_auth_success(self, get_ingredients):
        order_data = {"ingredients": create_order_data(get_ingredients)}
        headers = {"Content-type": "application/json"}
        response = requests.post(Urls.ORDERS_URL, headers=headers, json=order_data)
        assert response.status_code == TestCode.SUCCESS_CODE and TestMessage.MESSAGE_SUCCESS in response.text

    @allure.title('Проверка создания заказа без ингредиентов')
    def test_order_create_without_ingredients_fail(self, get_token):
        order_data = {"ingredients": []}
        token = get_token
        headers = {"Content-type": "application/json", "Authorization": f'{token}'}
        response = requests.post(Urls.ORDERS_URL, headers=headers, json=order_data)
        assert response.status_code == TestCode.BAD_REQUEST_CODE and response.json()['message'] == TestMessage.MESSAGE_CREATE_ORDER_BAD_REQUEST

    @allure.title('Проверка создания заказа с неверным хешем ингредиентов')
    def test_order_create_invalid_ingredients_fail(self, get_token):
        order_data = {"ingredients": ['invalid_ingredients_1','invalid_ingredients_2']}
        token = get_token
        headers = {"Content-type": "application/json", "Authorization": f'{token}'}
        response = requests.post(Urls.ORDERS_URL, headers=headers, json=order_data)
        assert response.status_code == TestCode.SERVER_ERROR_CODE and TestMessage.MESSAGE_CREATE_ORDER_INTERNAL_SERVER_ERROR in response.text