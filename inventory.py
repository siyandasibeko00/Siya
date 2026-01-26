class Shoes:
    def __init__(self, country, code, product, cost, quantity):
        self.country = country
        self.code = code
        self.product = product
        self.cost = float(cost)
        self.quantity = int(quantity)
        self.value = self.cost * self.quantity

    def get_cost(self):
        return self.cost
    
    def get_quantity(self):
        return self.quantity
    
    def __str__(self):
        return f"Country: {self.country}, Code: {self.code}, Product: {self.product}, Cost: {self.cost}, Quantity: {self.quantity}, Value: {self.value}"

shoes_list = []

def read_shoes_data():
    try:
        with open ("inventory.txt", "r") as file:
            lines = file.readlines() #read lines from inventory text file into new file
            for line in lines [1:]: #iterate through lines by starting from the second element and skipping the heading
                strip_lines = lines.strip() #removes whitespaces
                strip_lines = strip_lines.split(", ") #turns string into a list

            shoes_list.append(Shoes(strip_lines[0], strip_lines[1], strip_lines[2], strip_lines[3], strip_lines[4])) #add lines into empty list

    except FileNotFoundError:
        print('File "inventory.txt" does not exist')

def capture_shoes():

    print("Create your shoe")
    while True: #iterates until required condition is met/true
        try:
            country = input("Enter the country: ")
            code = input("Enter the code: ")
            product = input("Enter the name of the product: ")
            cost = float(input("Enter the cost: "))
            quantity = int(input("Enter the quantity: "))

            new_shoe = Shoes(country, code, product, cost, quantity) # create new shoe object
            shoes_list.append(new_shoe) #add the shoe created by the user to the list
            print(f"Successfully added new shoe: {new_shoe}")
        except ValueError:
            print("Invalid entry. Please try again.")
        
def view_all():
 
    if not shoes_list: #if shoes not in the list print message
        print("The shoe is not in the list.")
    else:
        for shoe in shoes_list: #if the shoes is in the list print details of the shoe
            print(shoe)
view_all() #call the function

def re_stock():
    # 1. Find the shoe with the lowest quantity
    lowest_quantity = min(shoes_list, key=lambda shoe: shoe.quantity) #function to return the minimum /smallest item in a list

    print(f"Re-stock Item:")
    print(f"Shoe: {lowest_quantity.code} ({lowest_quantity.product}), Current Qty: {lowest_quantity.quantity}") #print the code, product name and quantity of the item with lowest quantity

    # 3. Ask for Confirmation
    confirm = input("Add more stock for this item? (yes/no): ")

    if confirm == 'yes':
            add_amount = int(input(f"How many pairs to add to {lowest_quantity.code}? "))

            lowest_quantity.quantity += add_amount
            print(f"Item added to stock. New quantity: {lowest_quantity.quantity}") #if yes entered then new stock is loaded to the existing list and print 
    else:
        print("Restock cancelled for this item.") #if no is entered then no new stock is loaded on the list

def update_file(): #code to update existing inventory file
    with open("inventory.txt", "w+") as f:
        f.write("Country,Code,Product,Cost,Quantity")
        for shoe in shoes_list:
            f.write(f"{shoe.country},{shoe.code},{shoe.product},{shoe.cost},{shoe.quantity}")

def search_shoe(): 

    search_code = input("Enter code for the product you searching for: ")

    for shoe in shoes_list: #iterates over shoe_list and returns product if code entered matches code of product
        if shoe.code == search_code:
            return shoe
    else: #if code not in list then nothing is returned
        return None

def value_per_item(): 

    print("Total value of item")
    for shoe in shoes_list: #iterates over shoes_list
        value = shoe.cost * shoe.quantity #cost * quantity of shoe gives us the total value
        print(f"Product: {shoe.product} Total Value of product: {value}") #prints the product and its total value

def highest_qty():

    # Find the product with the maximum quantity
    highest_qty_shoe = max(shoes_list, key=lambda shoe: shoe.quantity)
    
    # Print the shoe as being for sale
    print(f"Product with highest quantity for sale: "
          f"{highest_qty_shoe.product}, Quantity: {highest_qty_shoe.quantity}")

def mainmenu(): #menu printed for the user to select numerical options
    print("1. Select file to read from")
    print("2. Create your shoe")
    print("3. See created shoe")
    print("4. Add number of shoes")
    print("5. Search for shoe")
    print("6. Get total value of item")
    print("7. Shoe for sale")
    print("8. Quit")

while True:
    option = input("Enter your option on menu: ")
    if option == 1:
        read_shoes_data()
    elif option == 2:
        capture_shoes()
    elif option == 3:
        view_all()
    elif option == 4:
        re_stock()
    elif option == 5:
        search_shoe()
    elif option == 6:
        value_per_item()
    elif option == 7:
        highest_qty()
    else:
        break

mainmenu()  