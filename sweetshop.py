class SweetShop:
    def __init__(self):
        self.sweets = {}

    def add_sweet(self, sweet):
        required_fields = ["id", "name", "category", "price", "quantity"]
        for field in required_fields:
            if field not in sweet:
                raise ValueError(f"Missing required field: {field}")

        if sweet["id"] in self.sweets:
            raise ValueError(f"Sweet with ID {sweet['id']} already exists.")
        
        
        self.sweets[sweet["id"]] = sweet

    def delete_sweet(self, sweet_id):
        if sweet_id not in self.sweets:
            raise ValueError(f"Sweet with ID {sweet_id} not found.")
            
        del self.sweets[sweet_id]
        return "Sweet deleted successfully."
    
    def delete_sweet(self, sweet_id):
        if sweet_id not in self.sweets:
            raise ValueError("Sweet not found.")
        del self.sweets[sweet_id]
        return "Sweet deleted successfully."

    def view_sweets(self):
        return self.sweets # Minimal implementation
    
    def view_sweets(self):
        if not self.sweets:
            raise ValueError("No sweets available in the shop.")
        return self.sweets
    
    def search_sweets(self, name=None, category=None, price_range=None):
        results = {}
        for sweet_id, sweet_details in self.sweets.items():
            if name and name.lower() in sweet_details['name'].lower():
                results[sweet_id] = sweet_details
        return results
    
    def search_sweets(self, name=None, category=None, price_range=None):
        results = {}
        for sweet_id, sweet_details in self.sweets.items():
            match = True
            if name and name.lower() not in sweet_details['name'].lower():
                match = False
            if category and category.lower() != sweet_details['category'].lower():
                match = False
            if match: # Only add if all conditions met so far
                results[sweet_id] = sweet_details
        return results
    
    def search_sweets(self, name=None, category=None, price_range=None):
        results = {}
        for sweet_id, sweet_details in self.sweets.items():
            match = True
            if name and name.lower() not in sweet_details['name'].lower():
                match = False
            if category and category.lower() != sweet_details['category'].lower():
                match = False
            if price_range:
                min_price, max_price = price_range
                if not (min_price <= sweet_details['price'] <= max_price):
                    match = False
            if match:
                results[sweet_id] = sweet_details
        return results
    
    def purchase_sweet(self, sweet_id, quantity):
        sweet = self.sweets[sweet_id] # Minimal implementation, assumes ID and sufficient quantity
        sweet['quantity'] -= quantity
        return "Sweet purchased successfully."
    
    def purchase_sweet(self, sweet_id, quantity):
        sweet = self.sweets[sweet_id]
        if sweet['quantity'] < quantity:
            raise ValueError("Not enough stock available.")
            
        sweet['quantity'] -= quantity
        return "Sweet purchased successfully."
    
    def purchase_sweet(self, sweet_id, quantity):
        if sweet_id not in self.sweets:
            raise ValueError("Sweet not found.")
            
        sweet = self.sweets[sweet_id]
        if sweet['quantity'] < quantity:
            raise ValueError("Not enough stock available.")
            
        sweet['quantity'] -= quantity
        return "Sweet purchased successfully."