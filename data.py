class Url:
    BASE_URL = 'https://qa-scooter.praktikum-services.ru'
    COURIER_URL = '/api/v1/courier'
    LOGIN_COURIER_URL = '/api/v1/courier/login'
    CREATE_ORDER_URL = '/api/v1/orders'
    LIST_ORDERS_URL = '/api/v1/orders'

class DataForCreateCourier:
    CREATE_COURIER_BODY = {
    "login": "ninja",
    "password": "1234",
    "firstName": "saske"
}

class DataForCreateOrder:
    CREATE_ORDER_BODY = {
        "firstName": "Naruto",
        "lastName": "Uchiha",
        "address": "Konoha, 142 apt.",
        "metroStation": 4,
        "phone": "+7 800 355 35 35",
        "rentTime": 5,
        "deliveryDate": "2020-06-06",
        "comment": "Saske, come back to Konoha",
        "color": [
            "BLACK"
        ]
    }