import requests
from data import Url
import allure

class OrderMethods:
    @staticmethod
    @allure.step('Дернуть ручку на создание заказа')
    def create_order(body):
        return requests.post(f'{Url.BASE_URL}{Url.CREATE_ORDER_URL}', json=body)

    @staticmethod
    @allure.step('Дернуть ручку на получение списка заказов')
    def check_list_orders():
        return requests.get(f'{Url.BASE_URL}{Url.LIST_ORDERS_URL}')

    @staticmethod
    @allure.step('Дернуть ручку на отмену заказа')
    def cancel_order(body):
        return requests.put(f'{Url.BASE_URL}{Url.CANCEL_ORDER}', json=body)

