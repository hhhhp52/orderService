from typing import Dict
from models.models import Address, Order
from utils import helpers


def create_order_impl(data: dict) -> (bool, Dict):
    result = dict(
        data=dict(),
        message="",
    )
    try:
        address = Address(data['address']['city'], data['address']['district'], data['address']['street'])
        order = Order(data['id'], data['name'], address, data['price'], data['currency'])

        flag, reason = helpers.check_name(order.name)
        if not flag:
            result['message'] = reason
            return False, result
        flag, reason = helpers.check_supported_currency(order.get_currency())
        if not flag:
            result['message'] = reason
            return False, result
        flag, reason = helpers.check_price(order.get_price(), order.get_currency())
        if not flag:
            result['message'] = reason
            return False, result

        result['data'] = {
            "order_id": order.order_id,
            "name": order.name,
            "address": {
                "city": order.address.city,
                "district": order.address.district,
                "street": order.address.street
            },
            "price": order.get_price(),
            "currency": order.get_currency()
        }

        return True, result
    except Exception as e:
        result['message'] = str(e)
        return False, result
