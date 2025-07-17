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

    def test_view_sweets_basic(self):
        # Test viewing available sweets
        sweet1 = {"id": "1", "name": "Chocolate Bar", "category": "Chocolate", "price": 2.50, "quantity": 100}
        sweet2 = {"id": "2", "name": "Gummy Bears", "category": "Candy", "price": 1.75, "quantity": 150}
        self.shop.add_sweet(sweet1)
        self.shop.add_sweet(sweet2)
        available_sweets = self.shop.view_sweets() # This method doesn't exist yet
        self.assertEqual(available_sweets, {"1": sweet1, "2": sweet2})
    
    def test_view_no_sweets_available(self):
        # Test viewing sweets when none are available
        with self.assertRaises(ValueError) as cm:
            self.shop.view_sweets()
        self.assertEqual(str(cm.exception), "No sweets available in the shop.")


if __name__ == '__main__':
    unittest.main()
    