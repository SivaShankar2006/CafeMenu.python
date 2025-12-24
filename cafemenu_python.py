#Define the meanu of restaurant
menu={
    'Burger ':100,
    'Pasta':80,
    'Pizza':120,
    'Tea':20,
    'Coffee':50
}
#Greetings
print("Welcome to Paradise Cafe")
print("Burger :Rs120\nPasta  :Rs80\nPizza  :Rs120\n" \
"Tea    :Rs20\nCoffee :Rs50")

order_total=0
#total amount of orders

item_1=input("Enter the name of the item you want to order = ")
if item_1 in menu:
    order_total +=menu[item_1]
    print(f"Your item {item_1} has been addded to your order. ")
else:
    print(f"Ordered item {item_1} is not available!")

another_order=input("Do you want to addd another item? (Yes/No)")
if another_order=='Yes':
    item_2=input('Enter the name of second item = ')
    if item_2 in menu:
        order_total +=menu[item_2]
        print((f"item {item_2} has been ordered to order"))
    else:
        print(f'Item {item_2} is not available!')

print(f'The total amount of items ordered is {order_total}')

