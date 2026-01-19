grocery_inventory = {"Milk":("Dairy",3.50,8),"Eggs":("Dairy",5.50,30),"Bread":("Bakery",2.99,15),"Apples":("Produce",1.50,50)}
eggs_details = grocery_inventory.get("Eggs")
print(eggs_details)
eggs_price = eggs_details.get[1]
print(eggs_price)
#bread_details = grocery_inventory.get("Bread")
#print("Details of Bread:",bread_details)
#grocery_inventory.update({"Cookies":(143,"Bakery")})
#print("Inventory after adding Cookies:",grocery_inventory)
#grocery_inventory.pop("Eggs")
#print("Inventory after removing eggs:",grocery_inventory)