import allure
import pytest
import helper



class TestCreateOrder:
    @allure.title('В заказе можно указать разные комбинации цвеом либо не указывать вообще')
    @pytest.mark.parametrize('selected_color', [
        ['BLACK'],
        ['GREY'],
        ['BLACK', 'GREY'],
        []
    ])
    def test_order_with_black_color(self, order_method, selected_color):
        body = helper.modify_create_order_body('color', selected_color)
        response = order_method.create_order(body)
        response_json = response.json()
        assert response.status_code == 201 and 'track' in response_json




