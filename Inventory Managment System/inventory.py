import pandas as pd
import product
class InventoryManagementSystem:
    def __init__(self, file_name='inventory.csv'):
        self.inventory = {}
        self.file_name = file_name
        self.load_inventory()

    def add_product(self, product_id, name, price, quantity):
        if product_id in self.inventory:
            print("Product with this ID already exists.")
        else:
            self.inventory[product_id] = product.Product(product_id, name, price, quantity)
            self.save_inventory()
            print("Product added successfully.")

    def update_product(self, product_id, field, new_value):
        if product_id in self.inventory:
            product = self.inventory[product_id]
            if hasattr(product, field):
                setattr(product, field, new_value)
                self.save_inventory()
                print("Product updated successfully.")
            else:
                print("Invalid field name.")
        else:
            print("Product not found.")

    def delete_product(self, product_id):
        if product_id in self.inventory:
            del self.inventory[product_id]
            self.save_inventory()
            print("Product deleted successfully.")
        else:
            print("Product not found.")

    def display_products(self):
        for product_id, product in self.inventory.items():
            print(f"Product ID: {product_id}, Name: {product.name}, Price: {product.price}, Quantity: {product.quantity}")

    def load_inventory(self):
        try:
            data = pd.read_csv(self.file_name)
            for index, row in data.iterrows():
                self.inventory[row['product_id']] = product.Product(row['product_id'], row['name'], row['price'], row['quantity'])
        except FileNotFoundError:
            print("No inventory data found. Starting with an empty inventory.")

    def save_inventory(self):
        data = {'product_id': [], 'name': [], 'price': [], 'quantity': []}
        for product_id, product in self.inventory.items():
            data['product_id'].append(product_id)
            data['name'].append(product.name)
            data['price'].append(product.price)
            data['quantity'].append(product.quantity)
        df = pd.DataFrame(data)
        df.to_csv(self.file_name, index=False)
