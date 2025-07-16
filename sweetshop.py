class SweetShop:
    def __init__(self):
        self.sweets = {}

    def add_sweet(self, sweet):
        required_fields = ["id", "name", "category", "price", "quantity"]
        for field in required_fields:
            if field not in sweet:
                raise ValueError(f"Missing required field: {field}")
        self.sweets[sweet["id"]] = sweet
    