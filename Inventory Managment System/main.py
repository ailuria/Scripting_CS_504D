import inventory
def main():
    ims = inventory.InventoryManagementSystem()
    while True:
        print("\nOptions:")
        print("1. Add a new product")
        print("2. Update product details")
        print("3. Delete a product")
        print("4. Display available products")
        print("5. Quit")
        choice = input("Enter your choice: ")
        
        if choice == '1':
            product_id = input("Enter product ID: ")
            name = input("Enter product name: ")
            price = float(input("Enter product price: "))
            quantity = int(input("Enter product quantity: "))
            ims.add_product(product_id, name, price, quantity)
        elif choice == '2':
            product_id = input("Enter product ID: ")
            field = input("Enter the field to update (name, price, quantity): ")
            new_value = input(f"Enter new value for {field}: ")
            ims.update_product(product_id, field, new_value)
        elif choice == '3':
            product_id = input("Enter product ID to delete: ")
            ims.delete_product(product_id)
        elif choice == '4':
            ims.display_products()
        elif choice == '5':
            break
        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == '__main__':
    main()