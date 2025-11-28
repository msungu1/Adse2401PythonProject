#python script/file to demonstarte how to read and display a json file
# data/contents

# import the required module

import json

# open the burger_sales.json file in the read mode and display its contents

with open("../files/burger_sales.json", "r") as json_file:
    burger_sales = json.load(json_file)


    # use a for loop to display the sales in the menu

    # Useafor loop to display the sales in the menu
print("Burger Sales Menu:\n")
for burger_sale in burger_sales:
    # Assuming each entry is a dictionary with keys like 'burger', 'price', 'quantity'
    burger = burger_sale.get("burger", "Unknown")
    price = burger_sale.get("price", "N/A")
    quantity = burger_sale.get("quantity", "N/A")
    print(f"Burger: {burger}, Price: {price}, Quantity Sold: {quantity}")
        