import unittest
from sweetshop import SweetShop

class TestSweetShop(unittest.TestCase):
    def setUp(self):
        # This method runs before each test, ensuring a clean state
        self.shop = SweetShop()

    # Tests will be added here following TDD

if __name__ == '__main__':
    unittest.main()
    