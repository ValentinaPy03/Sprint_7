from data import DataForCreateCourier, DataForCreateOrder

def modify_create_courier_body(key, value):
    body = DataForCreateCourier.CREATE_COURIER_BODY.copy()
    body[key] = value
    return body

def modify_create_order_body(key, value):
    body = DataForCreateOrder.CREATE_ORDER_BODY.copy()
    body[key] = value
    return body