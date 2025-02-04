from http.client import responses

import allure
from generators import generate_incorrect_password, generate_incorrect_login
from tests.conftest import courier_method

class TestLoginCourier:
    @allure.title('Тест Курьер может авторизоваться и запрос возвращает id')
    def test_successful_auth_2(self, courier_method, generate_courier_data):
        courier_method.create_courier(generate_courier_data[0])
        courier_log = courier_method.log_courier(generate_courier_data[1], generate_courier_data[2])
        response = courier_log.json()
        assert courier_log.status_code == 200 and 'id' in response

    @allure.title('Тест Ошибка при авторизации с неверным паролем')
    def test_auth_with_non_existent_password(self, courier_method, generate_courier_data):
        courier_method.create_courier(generate_courier_data[0])
        courier_log = courier_method.log_courier(generate_courier_data[1], generate_incorrect_password())
        assert courier_log.status_code == 404 and (courier_log.json()['message'] == "Учетная запись не найдена")

    @allure.title('Тест Ошибка при отсутствии поля логин')
    def test_auth_without_login(self, courier_method, generate_courier_data):
        courier_method.create_courier(generate_courier_data[0])
        courier_log = courier_method.log_courier(None, generate_courier_data[2])
        assert courier_log.status_code == 400 and (courier_log.json()['message'] == "Недостаточно данных для входа")

    @allure.title('Тест Ошибка при авторизации под несуществующим пользователем')
    def test_auth_with_non_existent_user(self, courier_method, generate_courier_data):
        courier_method.create_courier(generate_courier_data[0])
        courier_log = courier_method.log_courier(generate_incorrect_login(), generate_incorrect_password())
        assert courier_log.status_code == 404 and (courier_log.json()['message'] == "Учетная запись не найдена")



