import allure

class TestListOrders:
    @allure.title('Тест Получение списка заказов')
    def test_get_list_orders(self, order_method):
        list_orders = order_method.check_list_orders()
        response = list_orders.json()
        assert list_orders.status_code == 200 and ('orders' in response)