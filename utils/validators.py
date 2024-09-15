from abc import abstractmethod, ABC


class Validator(ABC):
    @abstractmethod
    def validate(self, data):
        pass


class CreateOrderValidator(Validator):
    def validate(self, data):
        required_fields = {
            'id': str,
            'name': str,
            'address': dict,
            'price': str,
            'currency': str
        }
        address_fields = {
            'city': str,
            'district': str,
            'street': str
        }

        for field, field_type in required_fields.items():
            if field not in data:
                return False, f"Missing field: {field}"
            if not isinstance(data[field], field_type):
                return False, f"Incorrect type for field: {field}, expected {field_type.__name__}"

        for field, field_type in address_fields.items():
            if field not in data['address']:
                return False, f"Missing field in address: {field}"
            if not isinstance(data['address'][field], field_type):
                return False, f"Incorrect type for field in address: {field}, expected {field_type.__name__}"

        return True, ""
