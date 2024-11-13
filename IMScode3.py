#Inventory Management System:

users = {
    "admin": {"password": "admin789", "role": "Admin"},
    "user": {"password": "user123", "role": "User"}
}
# Admins inventory:
inventory : list = []      #The List of inventory products
#Customer's cart:
Customer_cart : list = []   #The List of products in customer's cart 

low_stock_threshold = 5     #least threshold for stock 

class Users:
    def login(self):
        self.username = input('Enter your username:')
        self.password = input('Enter your password:')
        if self.username in users and users[self.username]["password"] == self.password:
            return users[self.username]["role"]
        else:
            print('Invalid credentials!')
            return None
        
# Customer Section:
class Customer:
#Customer's functions
    def AddtoCart(self):
        self.product_name : str = str(input('Enter the name of the product: '))
        for i, product in enumerate(inventory):
            if product['name'] == self.product_name :
                try:
                    self.prod_quantity = int(input('Enter the number of packets: '))
                    Customer_cart.append({'name' : self.product_name, 'quantity': self.prod_quantity})
                except ValueError as e:
                    print(f'Input Value error: {e}')
                print('The product has been added successfully!')   #When the product has been succesfullly added.
                return 
        print('Product not in the inventory!')

    def ViewCart(self):
        print('Your Cart:')
        if not Customer_cart:
            print('\nYour Cart is empty!')
        else:
            for product in Customer_cart:
                print(product)

# Admin Section:
class Admin:
#Admin Functions    
    def add_prod(self):
        try:
            self.prod_name = (input('Enter the name of the product: '))
            self.price : float = float(int(input('Enter the price of one pack of the product: ')))
            self.serial_no : int = int(input('Enter the serial number of the product: '))
            self.quantity : int = int(input('Enter the number of packets of the product: '))
            inventory.append({'name' : self.prod_name, 'price' : self.price, 'serial_num': self.serial_no, 'quantity': self.quantity})
            print('You have added a New Product!')
        except ValueError as e:
            print(f'Error occured {e}')
            print('Try entering the values again!\n')
            self.add_prod()

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
                try:
                    product['price'] = float(input('Enter the new price of the product: '))
                    product['serial_num'] = int(input('Enter the new serial number: '))
                    print('Product has been updated successfully!')
                except ValueError as e:
                    print(f'Error occured {e}')
                    print('Try entering the values again!\n')
                    self.edit_product()
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
        self.prod_name : str = str(input('Enter the name of the product: '))
        for i, product in enumerate(inventory):
            if product['name'] == self.prod_name:
                inventory.pop(i)
                print('The product has been removed successfully!')
                return 
        print('Product not in the inventory!')

def main():
    role = Users().login()
    if role is None:
        return
    
    while True:
        if role == "Admin":
            print('\nWelcome to Inventory Management System!')
            print("\n1. Add Product\n2. Edit Product\n3. Delete Product\n4. View Inventory\n5. Check Stock level\n6. Logout\n7. Close the Program")
            choice = input("Choose an option: ")
            if choice == '1':
                Admin().add_prod()
            elif choice =='2':
                Admin().edit_product()
            elif choice == '3':
                Admin().del_prod()
            elif choice == '4':
                Admin().view_inventory()
            elif choice == '5':
                Admin().check_stock_lev()
            elif choice == '6':
                print("Logged out.\n")
                main()
            elif choice == '7':
                print('Closing the Program.\n')
                exit()
            else:
                print("Invalid option.")
        
        elif role == "User":
            print('\nWelcome to Online Shopping Mart!')
            print("\n1. View Inventory. \n2. Add Product to your Cart. \n3. View your Cart. \n4. Logout \n5. Close the Program")
            choice = input("Choose an option: ")
            if choice == "1":
                Admin().view_inventory()
            elif choice == "2":
                Customer().AddtoCart()
            elif choice == '3':
                Customer().ViewCart()
            elif choice == '4':
                print('You have been logged out!\n')
                main()
            elif choice == '5':
                print('Closing the program. Thank you for shopping with us!')
                exit()
            else:
                print("Invalid option.")

if __name__ == "__main__":
    main()