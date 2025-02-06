import pytest
from generators import generate_courier_body, generate_courier_body_without_login
from methods.courier_methods import CourierMethods
from methods.order_methods import OrderMethods


@pytest.fixture()
def courier_method():
    return CourierMethods()

@pytest.fixture()
def order_method():
    return OrderMethods()

@pytest.fixture()
def generate_courier_data():
    courier_body = generate_courier_body()
    login = courier_body['login']
    password = courier_body['password']
    firstname = courier_body['firstName']
    yield [courier_body, login, password, firstname]
    courier_id = CourierMethods().courier_id_by_password_and_login(login, password)
    CourierMethods().delete_courier(courier_id)


@pytest.fixture()
def generate_courier_data_without_required_field():
    courier_body = generate_courier_body_without_login()
    password = courier_body['password']
    yield [courier_body, password]

