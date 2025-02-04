import allure
from generators import generate_courier_body, generate_courier_body_with_same_login
from tests.conftest import courier_method

class TestCreateCourier:
    @allure.title('Тест успешное создание курьера')
    def test_successful_create_courier(self, generate_courier_data, courier_method):
        courier = courier_method.create_courier(generate_courier_data[0])
        assert courier.status_code == 201 and (courier.json() == {'ok': True})

    @allure.title('Тест Нельзя создать 2 одинаковых курьеров')
    def test_create_same_courier(self, courier_method, generate_courier_data):
        courier_method.create_courier(generate_courier_data[0])
        courier_2 = courier_method.create_courier(generate_courier_data[0])
        assert courier_2.status_code == 409 and (courier_2.json()['message'] == 'Этот логин уже используется. Попробуйте другой.')

    @allure.title('Тест Ошибка при создании курьера без необходимого поля')
    def test_create_courier_without_required_field(self, courier_method, generate_courier_data_without_required_field):
        courier = courier_method.create_courier(generate_courier_data_without_required_field[0])
        assert courier.status_code == 400 and (courier.json()['message'] == "Недостаточно данных для создания учетной записи")

    @allure.title('Тест Ошибка при создании курьера с повторяющися логином')
    def test_create_courier_with_same_login(self, courier_method):
        courier_data_1 = generate_courier_body()
        courier_method.create_courier(courier_data_1)
        courier_data_2 = generate_courier_body_with_same_login(courier_data_1["login"])

        courier_2 = courier_method.create_courier(courier_data_2)
        assert courier_2.status_code == 409 and (courier_2.json()['message'] == 'Этот логин уже используется. Попробуйте другой.')

        with allure.step('Удалить созданного для теста курьера'):
            courier_id_1 = courier_method.courier_id_by_password_and_login(courier_data_1["login"], courier_data_1["password"])
            courier_method.delete_courier(courier_id_1)





