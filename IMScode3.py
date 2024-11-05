#Inventory Management System: Try 3

users = {
    "admin": {"password": "admin789", "role": "Admin"},
    "user": {"password": "user123", "role": "User"}
}

inventory : list = []      #The List of inventory products

low_stock_threshold = 5

class Users:
    def login(self):
        self.username = input('Enter your username:')
        self.password = input('Enter your password:')
        if self.username in users and users[self.username]["password"] == self.password:
            return users[self.username]["role"]
        else:
            print('Invalid credentials!')
            return None

class Admin:
#Admin Functions    
    def add_prod(self):
        self.prod_name = (input('Enter the name of the product: '))
        self.price : float = float(int(input('Enter the price of the product: ')))
        self.serial_no : int = int(input('Enter the serial number of the product: '))
        self.quantity : int = int(input('Enter the quantity of the product: '))
        inventory.append({'name' : self.prod_name, 'price' : self.price, 'serial_num': self.serial_no, 'quantity': self.quantity})
        print('You have added a New Product!')

    def view_inventory(self):
        if not inventory:
            print('The inventory is empty!')
        else:
            print('\nCurrent Inventory:')
            for product in inventory:
                print(product)
                if product['quantity'] <= low_stock_threshold:
                    print(f'Warning Alert! ${product['name']} is running low on stock! Consider restocking')
        
    def edit_product(self):
        self.prod_name = input('Enter the name of the product: ')
        for product in inventory:
            if product['name'] == self.prod_name:
                product['price'] = float(input('Enter the new price of the product: '))
                product['serial_no'] = int(input('Enter the new serial number: '))
                print('Product has been updated successfully!')
                return
        print('Product not found!')

    def check_stock_lev(self):
        print('\nLow Stock Products: ')
        low_stock_prod = [prod for prod in inventory if prod['quantity'] <= low_stock_threshold]
        if not low_stock_prod:
            print("No products with low stock.")
        else:
            for product in low_stock_prod:
                print(product)

            
    def del_prod(self):
        self.prod_name = input('Enter the name of the product: ')
        for product in inventory:
            if product['name'] in inventory == self.prod_name:
                product.remove()
                print('The product has been removed successfully!')
                return 
        print('Product not in the inventory!')

    def main(self):
        role = Users().login()
        if role is None:
            return
        
        while True:
            if role == "Admin":
                print("\n1. Add Product\n2. Edit Product\n3. Delete Product\n4. View Inventory\n5. Check Stock level\n6. Logout")
                choice = input("Choose an option: ")
                if choice == '1':
                    self.add_prod()
                elif choice =='2':
                    self.edit_product()
                elif choice == '3':
                    self.del_prod()
                elif choice == '4':
                    self.view_inventory()
                elif choice == '5':
                    self.check_stock_lev()
                elif choice == '6':
                    print("Logged out.")
                    break
                else:
                    print("Invalid option.")
            
            elif role == "User":
                print("\n1. View Inventory\n2. Logout")
                choice = input("Choose an option: ")
                if choice == "1":
                    self.add_prod()
                elif choice == "2":
                    print("Logged out.")
                    break
                else:
                    print("Invalid option.")

if __name__ == "__main__":
    Admin().main()