from flask import Flask, request

from implement import implement
from utils.helpers import make_failed_response, make_success_response
from utils.validators import CreateOrderValidator

app = Flask(__name__)


@app.route('/api/orders', methods=['POST'])
def create_order():
    data = request.get_json()
    validator = CreateOrderValidator()
    is_valid, message = validator.validate(data)
    if not is_valid:
        return make_failed_response(data=dict(), reason=message)

    flag, result = implement.create_order_impl(data)

    if not flag:
        return make_failed_response(
            reason=result.get("message")
        )

    return make_success_response(
        data=result.get("data"),
        reason=result.get("message")
    )


if __name__ == '__main__':
    app.run()
