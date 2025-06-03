import pytest
import allure
import requests

from helpers import *
from data import *


@allure.feature('Получение заказов конкретного пользователя')
class TestOrdersUser:
    @allure.title('Проверка получения заказов авторизованного пользователя')
    def test_get_orders_user_auth_success(self, get_token, get_ingredients):
        order_data = {"ingredients": create_order_data(get_ingredients)}
        token = get_token
        headers = {"Content-type": "application/json", "Authorization": f'{token}'}
        response = requests.get(Urls.ORDERS_URL, headers=headers, json=order_data)
        assert response.status_code == TestCode.SUCCESS_CODE and TestMessage.MESSAGE_SUCCESS in response.text

    @allure.title('Проверка получения заказов неавторизованного пользователя')
    def test_get_orders_user_without_auth_fail(self):
        headers = {"Content-type": "application/json"}
        response = requests.get(Urls.ORDERS_URL, headers=headers)
        assert response.status_code == TestCode.UNAUTHORIZED_CODE and response.json()['message'] == TestMessage.MESSAGE_ORDER_NUMBERS_UNAUTHORIZED