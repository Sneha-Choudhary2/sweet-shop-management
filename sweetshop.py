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
    
    def restock_sweet(self, sweet_id, quantity):
        if sweet_id not in self.sweets:
            raise ValueError("Sweet not found.")
            
        self.sweets[sweet_id]['quantity'] += quantity
        return "Sweet restocked successfully."
        

    def main():
        shop = SweetShop()

        while True:
            print("\nSweet Shop Management System")
            print("A. Add Sweet")
            print("V. View All Sweets")
            print("D. Delete Sweet")
            print("S. Search Sweets")
            print("P. Purchase Sweet")
            print("R. Restock Sweet")
            print("E. Exit")

            choice = input("Enter your choice (A, V, D, S, P, R, E): ").upper()

            if choice == "A":
                sweet_id = input("Enter Sweet ID: ")
                name = input("Enter Name: ")
                category = input("Enter Category: ")
                try:
                    price = float(input("Enter Price: "))
                    quantity = int(input("Enter Quantity: "))
                    sweet = {"id": sweet_id, "name": name, "category": category, "price": price, "quantity": quantity}
                    shop.add_sweet(sweet)
                    print(f"Sweet '{name}' added successfully.")
                except ValueError as ve:
                    print(f"Invalid input: {ve}. Please ensure price and quantity are numbers.")
                except Exception as e:
                    print(f"Error: {e}")

            elif choice == "V":
                try:
                    all_sweets = shop.view_sweets()
                    print("\n--- Available Sweets ---")
                    for sweet_id, details in all_sweets.items():
                        print(f"ID: {sweet_id}, Name: {details['name']}, Category: {details['category']}, Price: ${details['price']:.2f}, Quantity: {details['quantity']}")
                    print("------------------------")
                except Exception as e:
                    print(f"Error: {e}")

            elif choice == "D":
                sweet_id = input("Enter ID of the sweet to delete: ")
                try:
                    result = shop.delete_sweet(sweet_id)
                    print(result)
                except Exception as e:
                    print(f"Error: {e}")

            elif choice == "S":
                print("\nSearch Options:")
                print("1. By Name")
                print("2. By Category")
                print("3. By Price Range")
                search_choice = input("Enter search option (1, 2, or 3): ")
                try:
                    results = {}
                    if search_choice == "1":
                        name = input("Enter name to search: ")
                        results = shop.search_sweets(name=name)
                    elif search_choice == "2":
                        category = input("Enter category to search: ")
                        results = shop.search_sweets(category=category)
                    elif search_choice == "3":
                        min_price = float(input("Enter minimum price: "))
                        max_price = float(input("Enter maximum price: "))
                        results = shop.search_sweets(price_range=(min_price, max_price))
                    else:
                        print("Invalid search option.")
                        continue

                    if not results:
                        print("No sweets found matching your criteria.")
                    else:
                        print("\n--- Search Results ---")
                        for sweet_id, details in results.items():
                            print(f"ID: {sweet_id}, Name: {details['name']}, Category: {details['category']}, Price: ${details['price']:.2f}, Quantity: {details['quantity']}")
                        print("----------------------")
                except ValueError:
                    print("Invalid input for price range. Please enter numbers.")
                except Exception as e:
                    print(f"Error: {e}")

            elif choice == "P":
                sweet_id = input("Enter ID of the sweet to purchase: ")
                try:
                    quantity = int(input("Enter quantity to purchase: "))
                    result = shop.purchase_sweet(sweet_id, quantity)
                    print(result)
                except ValueError as ve:
                    print(f"Error: {ve}")
                except Exception as e:
                    print(f"Error: {e}")

            elif choice == "R":
                sweet_id = input("Enter ID of the sweet to restock: ")
                try:
                    quantity = int(input("Enter quantity to restock: "))
                    result = shop.restock_sweet(sweet_id, quantity)
                    print(result)
                except ValueError as ve:
                    print(f"Error: {ve}")
                except Exception as e:
                    print(f"Error: {e}")

            elif choice == "E":
                print("Exiting the Sweet Shop Management System.")
                break

            else:
                print("Invalid choice. Please enter a valid option.")

    if __name__ == "__main__":
        main()
    
    
    