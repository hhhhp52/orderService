from decimal import Decimal
from typing import Dict

from flask import make_response, jsonify

from utils import constants


def make_failed_response(data=None, reason=None, status_code=400):
    return make_response(
        jsonify(
            data=data,
            reason=reason
        ),
        status_code
    )


def make_success_response(data=None, reason=None, status_code=200):
    return make_response(
        jsonify(
            data=data,
            reason=reason
        ),
        status_code
    )


def check_supported_currency(currency):
    if currency not in constants.SUPPORTED_CURRENCY:
        reason = "Currency format is wrong."
        return False, reason
    return True, ""


def check_price(price, currency):
    price = Decimal(price)
    reason = "Price is over 2000"
    if currency == constants.CURRENCY_USD:
        if price > round(constants.LIMIT_PRICE_SETTING_TWD / 31, 3):
            return False, reason
    else:
        if price > constants.LIMIT_PRICE_SETTING_TWD:
            return False, reason
    return True, ""


def check_name(name):
    if not all(char.isalpha() or char.isspace() for char in name):
        reason = "Name contains non-English characters."
        return False, reason
    # Check the name every word start with Upper case
    if not all([word.istitle() for word in name.split()]):
        reason = "Name is not capitalized."
        return False, reason
    return True, ""
