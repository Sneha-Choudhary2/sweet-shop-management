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

    def test_add_sweet_with_duplicate_id(self):
        # Test adding a sweet with an ID that already exists
        sweet = {"id": "1", "name": "Chocolate Bar", "category": "Chocolate", "price": 2.50, "quantity": 100}
        self.shop.add_sweet(sweet) # Add it once
        with self.assertRaises(ValueError) as cm:
            self.shop.add_sweet(sweet) # Try to add it again
        self.assertEqual(str(cm.exception), f"Sweet with ID {sweet['id']} already exists.")

    def test_delete_sweet_basic(self):
        # Test deleting an existing sweet
        sweet = {"id": "1", "name": "Chocolate Bar", "category": "Chocolate", "price": 2.50, "quantity": 100}
        self.shop.add_sweet(sweet)
        result = self.shop.delete_sweet("1") # This method doesn't exist yet
        self.assertEqual(result, "Sweet deleted successfully.")
        self.assertNotIn("1", self.shop.sweets)
    
    def test_delete_nonexistent_sweet(self):
        # Test deleting a sweet that does not exist
        with self.assertRaises(ValueError) as cm:
            self.shop.delete_sweet("nonexistent_id")
        self.assertEqual(str(cm.exception), "Sweet not found.")


if __name__ == '__main__':
    unittest.main()
    