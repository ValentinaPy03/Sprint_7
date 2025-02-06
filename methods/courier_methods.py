import requests
from data import Url
import allure

class CourierMethods:
    @staticmethod
    @allure.step('Дернуть ручку на создание курьера')
    def create_courier(body):
        return requests.post(f'{Url.BASE_URL}{Url.COURIER_URL}', json=body)

    @staticmethod
    @allure.step('Дернуть ручку на удаление курьера')
    def delete_courier(courier_id):
        return requests.delete(f'{Url.BASE_URL}{Url.COURIER_URL}/{courier_id}')

    @staticmethod
    @allure.step('Узнать id курьера через login и password')
    def courier_id_by_password_and_login(login, password):
        payload = {
            'login': login,
            'password': password
            }
        response = requests.post(f'{Url.BASE_URL}{Url.LOGIN_COURIER_URL}', json=payload)
        courier_id = response.json()
        return courier_id.get('id')

    @staticmethod
    @allure.step('Авторизоваться')
    def log_courier(login, password):
        payload = {
            'login': login,
            'password': password
        }
        return requests.post(f'{Url.BASE_URL}{Url.LOGIN_COURIER_URL}', json=payload)