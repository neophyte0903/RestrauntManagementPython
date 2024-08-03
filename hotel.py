"""## Restruant order app"""

menu={
    'sandwhich':100,
    'salad':200,
    'soda':50,
    'pizza':250,
    'burger':125
}

def showMenu():
    print(menu)

orderList=[]

def addOrder():
    item=input('enter a name from the menu')
    if item in menu:
        quantity=int(input('enter the quantity'))
        orderList.append((item,quantity))
        print(f'added {quantity} number of {item}')
    else:
        print('item not found')

def viewOrder():
    if not orderList:
        print('your pallate is empty')
        return
    print('your order list:')
    for item,quantity in orderList:
        print(f"{quantity} x {item} @ Rs{menu[item]:.2f} each")
    print()

def calculateTotal():
    total=sum(menu[item]* quantity for item,quantity in orderList)
    print('your total is: Rs',total)

while True:
    print('Welcome to mealsOnCloud')
    print("1. View Menu")
    print("2. Place an Order")
    print("3. View Your Order")
    print("4. Calculate Total")
    print("5. Exit")
    choice=input('enter your choice')

    if choice=='1':
        showMenu()
    if choice=='2':
        addOrder()
    if choice=='3':
        viewOrder()
    if choice=='4':
        calculateTotal()
    if choice=='5':
        print('thank you for visiting mealsoncloud')
        break;
