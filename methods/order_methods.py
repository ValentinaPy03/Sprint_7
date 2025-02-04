import requests
from data import Url

class OrderMethods:
    def create_order(self, body):
        return requests.post(f'{Url.BASE_URL}{Url.CREATE_ORDER_URL}', json=body)

    def check_list_orders(self):
        return requests.get(f'{Url.BASE_URL}{Url.LIST_ORDERS_URL}')


