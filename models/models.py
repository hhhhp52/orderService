from decimal import Decimal
from utils import constants


class Address:
    def __init__(self, city: str, district: str, street: str):
        self.city = city
        self.district = district
        self.street = street


class Order:
    def __init__(self, order_id: str, name: str, address: Address, price: str, currency: str):
        self.order_id = order_id
        self.name = name
        self.address = address
        self.price = price
        self.currency = currency

    def get_price(self):
        if self.currency == constants.CURRENCY_USD:
            return str(Decimal(self.price) * 31)
        return self.price

    def get_currency(self):
        if self.currency == constants.CURRENCY_USD:
            return constants.CURRENCY_TWD
        return self.currency
