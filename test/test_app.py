import unittest
from implement.implement import create_order_impl


class TestCreateOrder(unittest.TestCase):
    def test_create_order_success(self):
        data = {
            "id": "A0000001",
            "name": "Melody Holiday Inn",
            "address": {
                "city": "taipei-city",
                "district": "da-an-district",
                "street": "fuxing-south-road"
            },
            "price": "2000",
            "currency": "TWD"
        }
        success, result = create_order_impl(data)
        self.assertTrue(success)
        self.assertEqual(result['data']['name'], "Melody Holiday Inn")
        self.assertEqual(result['data']['price'], "2000")
        self.assertEqual(result['data']['currency'], "TWD")

    def test_create_order_invalid_name(self):
        data = {
            "id": "A0000001",
            "name": "Melody holiday Inn",
            "address": {
                "city": "taipei-city",
                "district": "da-an-district",
                "street": "fuxing-south-road"
            },
            "price": "2000",
            "currency": "TWD"
        }
        success, result = create_order_impl(data)
        self.assertFalse(success)
        self.assertEqual(result['message'], "Name is not capitalized.")

    def test_create_order_invalid_name_with_non_english_characters(self):
        data = {
            "id": "A0000001",
            "name": "Melody holiday-Inn",
            "address": {
                "city": "taipei-city",
                "district": "da-an-district",
                "street": "fuxing-south-road"
            },
            "price": "2000",
            "currency": "TWD"
        }
        success, result = create_order_impl(data)
        self.assertFalse(success)
        self.assertEqual(result['message'], "Name contains non-English characters.")

    def test_create_order_price_exceeds_twd(self):
        data = {
            "id": "A0000001",
            "name": "Melody Holiday Inn",
            "address": {
                "city": "taipei-city",
                "district": "da-an-district",
                "street": "fuxing-south-road"
            },
            "price": "2050",
            "currency": "TWD"
        }
        success, result = create_order_impl(data)
        self.assertFalse(success)
        self.assertEqual(result['message'], "Price is over 2000")

    def test_create_order_price_exceeds_usd(self):
        data = {
            "id": "A0000001",
            "name": "Melody Holiday Inn",
            "address": {
                "city": "taipei-city",
                "district": "da-an-district",
                "street": "fuxing-south-road"
            },
            "price": "70",
            "currency": "USD"
        }
        success, result = create_order_impl(data)
        self.assertFalse(success)
        self.assertEqual(result['message'], "Price is over 2000")

    def test_create_order_currency_conversion(self):
        data = {
            "id": "A0000001",
            "name": "Melody Holiday Inn",
            "address": {
                "city": "taipei-city",
                "district": "da-an-district",
                "street": "fuxing-south-road"
            },
            "price": "50",
            "currency": "USD"
        }
        success, result = create_order_impl(data)
        self.assertTrue(success)
        self.assertEqual(result['data']['price'], "1550")
        self.assertEqual(result['data']['currency'], "TWD")


if __name__ == '__main__':
    unittest.main()
