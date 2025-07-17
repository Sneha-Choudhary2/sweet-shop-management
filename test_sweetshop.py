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

    def test_search_sweets_by_name(self):
        sweet1 = {"id": "1", "name": "Chocolate Bar", "category": "Chocolate", "price": 2.50, "quantity": 100}
        sweet2 = {"id": "2", "name": "White Chocolate", "category": "Chocolate", "price": 3.00, "quantity": 50}
        self.shop.add_sweet(sweet1)
        self.shop.add_sweet(sweet2)
        results = self.shop.search_sweets(name="chocolate") # This method doesn't exist yet
        self.assertEqual(len(results), 2)
        self.assertIn("1", results)
        self.assertIn("2", results)

    def test_search_sweets_by_category(self):
        sweet1 = {"id": "1", "name": "Chocolate Bar", "category": "Chocolate", "price": 2.50, "quantity": 100}
        sweet2 = {"id": "2", "name": "Gummy Bears", "category": "Candy", "price": 1.75, "quantity": 150}
        self.shop.add_sweet(sweet1)
        self.shop.add_sweet(sweet2)
        results = self.shop.search_sweets(category="Candy")
        self.assertEqual(len(results), 1)
        self.assertIn("2", results)

    def test_search_sweets_by_price_range(self):
        sweet1 = {"id": "1", "name": "Chocolate Bar", "category": "Chocolate", "price": 2.50, "quantity": 100}
        sweet2 = {"id": "2", "name": "White Chocolate", "category": "Chocolate", "price": 3.00, "quantity": 50}
        sweet3 = {"id": "3", "name": "Gummy Bears", "category": "Candy", "price": 1.75, "quantity": 150}
        self.shop.add_sweet(sweet1)
        self.shop.add_sweet(sweet2)
        self.shop.add_sweet(sweet3)
        results = self.shop.search_sweets(price_range=(2.00, 3.00))
        self.assertEqual(len(results), 2)
        self.assertIn("1", results)
        self.assertIn("2", results)
        self.assertNotIn("3", results)

    def test_search_sweets_no_results(self):
        sweet1 = {"id": "1", "name": "Chocolate Bar", "category": "Chocolate", "price": 2.50, "quantity": 100}
        self.shop.add_sweet(sweet1)
        results = self.shop.search_sweets(name="Lollipop")
        self.assertEqual(len(results), 0)
    def test_search_sweets_empty_shop(self):
        results = self.shop.search_sweets(name="any")
        self.assertEqual(len(results), 0)

    def test_purchase_sweet_basic(self):
            # Test purchasing an available sweet
        sweet = {"id": "1", "name": "Chocolate Bar", "category": "Chocolate", "price": 2.50, "quantity": 100}
        self.shop.add_sweet(sweet)
        result = self.shop.purchase_sweet("1", 10) # This method doesn't exist yet
        self.assertEqual(result, "Sweet purchased successfully.")
        self.assertEqual(self.shop.sweets["1"]["quantity"], 90)

    def test_purchase_sweet_insufficient_stock(self):
            # Test purchasing more than available stock
        sweet = {"id": "1", "name": "Chocolate Bar", "category": "Chocolate", "price": 2.50, "quantity": 5}
        self.shop.add_sweet(sweet)
        with self.assertRaises(ValueError) as cm:
            self.shop.purchase_sweet("1", 10)
        self.assertEqual(str(cm.exception), "Not enough stock available.")
        self.assertEqual(self.shop.sweets["1"]["quantity"], 5) # Quantity should remain unchanged

    def test_purchase_nonexistent_sweet(self):
            # Test purchasing a sweet that does not exist
        with self.assertRaises(ValueError) as cm:
            self.shop.purchase_sweet("nonexistent_id", 5)
        self.assertEqual(str(cm.exception), "Sweet not found.")
    
    def test_restock_sweet_basic(self):
            # Test restocking an existing sweet
        sweet = {"id": "1", "name": "Chocolate Bar", "category": "Chocolate", "price": 2.50, "quantity": 100}
        self.shop.add_sweet(sweet)
        result = self.shop.restock_sweet("1", 50) # This method doesn't exist yet
        self.assertEqual(result, "Sweet restocked successfully.")
        self.assertEqual(self.shop.sweets["1"]["quantity"], 150)
if __name__ == '__main__':
    unittest.main()
    