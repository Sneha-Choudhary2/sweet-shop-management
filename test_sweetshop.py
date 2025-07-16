import unittest
from sweetshop import SweetShop

class TestSweetShop(unittest.TestCase):
    def setUp(self):
        # This method runs before each test, ensuring a clean state
        self.shop = SweetShop()

    def test_add_sweet_basic(self):
        # Test adding a valid sweet
        sweet = {"id": "1", "name": "Chocolate Bar", "category": "Chocolate", "price": 2.50, "quantity": 100}
        self.shop.add_sweet(sweet) # This method doesn't exist yet, so it will fail
        self.assertIn(sweet["id"], self.shop.sweets)
        self.assertEqual(self.shop.sweets["1"], sweet)
        
    def test_add_sweet_with_missing_fields(self):
        # Test adding a sweet with missing required fields
        incomplete_sweet = {"id": "2", "name": "Gummy Bears"} # Missing category, price, quantity
        with self.assertRaises(ValueError) as cm:
            self.shop.add_sweet(incomplete_sweet)
        self.assertIn("Missing required field:", str(cm.exception))

if __name__ == '__main__':
    unittest.main()
    