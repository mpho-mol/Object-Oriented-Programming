class Shoes:
    #constructor
    def __init__(self, country, code, product, cost, quantity):
        self.country = country
        self.code = code
        self.product = product
        self.cost = cost
        self.quantity = quantity

  
    #function to return the cost of the shoe
    def get_cost(self):
        return self.cost

    #function to return the quantity of the shoes
    def get_quanty(self):
        return self.quantity

    #function to return a string representing the Shoes class
    def __str__(self):
        return self.country + ", " + self.code + ", " + self.product + ", " + str(self.cost) + ", " + str(self.quantity)


#create a variable with an empty list, this variable will be used to store a list of shoes objects
shoes = []

# open the file inventory.txt and read the data from this file then create shoes object and append this object into the shoes list
def read_shoes_data():
    filename = r"C:\Users\User\Downloads\inventory.txt"
    try:
        line_no = 0
        with open(filename, "r") as f:
            # iterate though the file contents
            for line in f:
                if line_no != 0:
                    #storing the read data by spliting by ","
                    (country, code, product, cost, quantity) = line.rstrip('\n').strip().split(',')
                    shoes.append(Shoes(country, code, product, int(cost), int(quantity)))

                line_no += 1
        print("Read data from inventory.txt files")
    except IOError:
        print("File ", filename, " not accessible")

# this function will allow a user to capture
# data about a shoe and use this data to create a shoe object
# and append this object inside the shoe list.
def capture_shoes():
    s_country = input("Please enter country: ")
    s_code = input("Please enter code: ")
    s_product = input("Please enter product: ")
    s_cost = int(input("Please enter cost: "))
    s_quantity = int(input("Please enter quantity: "))

    # create a shoe object
    shoe = Shoes(s_country, s_code, s_product, s_cost, s_quantity)
    shoes.append(shoe)

#iterate over all the shoes list and print the details of the shoes
def view_all():
    for shoe in shoes:
        print(str(shoe))

#this function will find the shoe object with the lowest quantity, which is the shoes that need to be restocked
def re_stock():
    lowest_quantity = shoes[0]
    #iterate through the list
    for shoe in shoes:
        #check if quantity is lowest
        if shoe.get_quanty() < lowest_quantity.get_quanty():
            lowest_quantity = shoe

    print("Lowest Quantity Details\n"+str(lowest_quantity))

    # Ask the user if he wants to add the quantity of
    # these shoes and then update it
    need_restock = input("Do you want to add to quantity of shoes(yes/no)? ")
    if need_restock.lower() == "yes":
        quantity_to_update = int(input("Please enter quantity to update: "))
        lowest_quantity.quantity = lowest_quantity.get_quanty() + quantity_to_update
    else:
        print("You selected no need to restock.")



#function to search for a shoe from the list using the shoe code
def search_shoe(code):
    #iterate through the list
    for shoe in shoes:
        #check if code is same
        if shoe.code == code:
            return shoe

#calculate the total value for each item
def value_per_item():
    value = 0
    for shoe in shoes:
        value = shoe.get_cost() * shoe.get_quanty()

        print(str(shoe) +"\tValue: " + str(value))

    return value

# determine the product with the highest quantity and print this shoe as being for sale
def highest_qty():
    highest_quantity_shoe = shoes[0]
    # iterate through the list
    for shoe in shoes:
        # check if quantity is highest
        if shoe.get_quanty() > highest_quantity_shoe.get_quanty():
            highest_quantity_shoe = shoe

    print(str(highest_quantity_shoe))

if __name__ == '__main__':
    choice = 0
    while True:
        print("1. Read shoes data")
        print("2. Capture shoes")
        print("3. View all Shoes")
        print("4. Restock Shoes")
        print("5. Search Shoe")
        print("6. Get Total value of Stock")
        print("7. Quit")

        choice = int(input("Please enter choice: "))

        #based on user choice call relevant function
        if choice == 1:
            read_shoes_data()
        elif choice == 2:
            capture_shoes()
        elif choice == 3:
            view_all()
        elif choice == 4:
            re_stock()
        elif choice == 5:
            code = input("Enter code to be search? ")
            print(str(seach_shoe(code)))
        elif choice == 6:
            value_per_item()
        elif choice == 7:
            print("Thank you.")
            break
        else:
            print("Invalid choice")
