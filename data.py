class Url:
    BASE_URL = 'https://qa-scooter.praktikum-services.ru'
    COURIER_URL = '/api/v1/courier'
    LOGIN_COURIER_URL = '/api/v1/courier/login'
    CREATE_ORDER_URL = '/api/v1/orders'
    LIST_ORDERS_URL = '/api/v1/orders'
    CANCEL_ORDER = '/api/v1/orders/cancel'

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

class AnswerText:
    TEXT_POST_CREATE_COURIER = {'ok': True}
    TEXT_BUG_409_CREATE_COURIER = 'Этот логин уже используется. Попробуйте другой.'
    TEXT_BUG_400_CREATE_COURIER = "Недостаточно данных для создания учетной записи"
    TEXT_BUG_404_LOG_COURIER = "Учетная запись не найдена"
    TEXT_BUG_400_LOG_COURIER = "Недостаточно данных для входа"
