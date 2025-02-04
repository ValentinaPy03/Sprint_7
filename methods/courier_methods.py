import requests
from data import Url

class CourierMethods:
    def create_courier(self, body):
        return requests.post(f'{Url.BASE_URL}{Url.COURIER_URL}', json=body)

    def delete_courier(self, courier_id):
        return requests.delete(f'{Url.BASE_URL}{Url.COURIER_URL}/{courier_id}')

    def courier_id_by_password_and_login(self, login, password):
        payload = {
            'login': login,
            'password': password
            }
        response = requests.post(f'{Url.BASE_URL}{Url.LOGIN_COURIER_URL}', json=payload)
        courier_id = response.json()
        return courier_id.get('id')

    def log_courier(self, login, password):
        payload = {
            'login': login,
            'password': password
        }
        return requests.post(f'{Url.BASE_URL}{Url.LOGIN_COURIER_URL}', json=payload)