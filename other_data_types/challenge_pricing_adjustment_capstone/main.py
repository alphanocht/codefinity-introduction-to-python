grocery_inventory = {"Milk":("Dairy",3.50,8),"Eggs":("Dairy",5.50,30),"Bread":("Bakery",2.99,15),"Apples":("Produce",1.50,50)}
eggs_details = grocery_inventory.get("Eggs")
print(eggs_details)
eggs_price = (eggs_details[1])
if eggs_price > 5:
    print("Eggs are too expensive, reducing the price by $1.")
    grocery_inventory.update({"Eggs":("Dairy",4.50,30)})
else:
    print("The price of Eggs is reasonable")
#eggs_price = eggs_details.get[1]
print(grocery_inventory)
grocery_inventory.update({"Tomatoes":("Produce",1.20,30)})
print("Inventory after adding Tomatoes:",grocery_inventory)
milk_details = grocery_inventory.get("Milk")
print(milk_details)
milk_stock = (milk_details[2])
if milk_stock < 10:
    print("Milk needs to be restocked. Increasing stock by 20 units.")
    grocery_inventory.update({"Milk":("Dairy",3.50,28)})
else:
    print("MIlk has sufficient stock")
apples_details = grocery_inventory.get("Apples")
apples_price = (apples_details[1])
if apples_price > 2:
    print("Apples removed from inventory due to high price.")
    grocery_inventory.pop("Apples")
else:
     print("Updated inventory:",grocery_inventory)
#bread_details = grocery_inventory.get("Bread")
#print("Details of Bread:",bread_details)
#grocery_inventory.update({"Cookies":(143,"Bakery")})
#print("Inventory after adding Cookies:",grocery_inventory)
#grocery_inventory.pop("Eggs")
#print("Inventory after removing eggs:",grocery_inventory)
#bread = ["Bread", 4.80, 3, "Gluten Free"] # Item name, price, quantity, type
#milk = ["Milk", 5.99, 2, "2% Milk"]   # Item name, price, quantity, type
#apple = ["Apple", 1.27, 12, "Fuji"] # Item name, price, quantity, type

# Create the main grocery list that contains these items
#grocery_list = [bread, apple, milk]
#print("Grocery List:" , grocery_list)

# Accessing and printing specific item details using indexing
#print("Item:", grocery_list[2][0]) # Accesses "Milk" title
#print("Price:", grocery_list[2][1]) # Accesses price of a Milk, which is 5.99
#print("Quantity:", grocery_list[2][2]) # Accesses quantity of Milk, which is 2
#print("Type:", grocery_list[2][3]) # Accesses type of Milk, which is "2% Milk"
