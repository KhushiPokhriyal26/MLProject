from Admin import lst
cart={}
def view_products():
    print("\nProducts \t Prices")
    for i,j in lst.items():
        print("\n{0} \t {1}\n".format(i,j))

def basket():
    name=str(input("Enter the item to be added to the cart -> "))
    if name in lst.keys():
        quantity=int(input("Enter the quantity -> "))
        cart[name]=quantity
        print("Item added")
    else:
        print("item not in stock")

def view_basket():
    print("\ncart item:-\nItems \t Quantity\n ")
    for i,j in cart.items():
        print("\n{0} \t {1}\n".format(i,j))

def search():
    name=str(input("Enter the name of the item to search -> "))
    if name in lst.keys():
        print("{0}\t{1}".format(name,lst[name]))
    else:
        print("the item is not in stock")

def remove():
    name=str(input("Enter the name of the item to remove from the basket-> "))
    if name in cart.keys():
        del cart[name]
    else:
        print("NO such item in cart")

def print_invoice():
    sum=0
    print("\nThe items in the cart are :-")
    print("\nItem \t Quantity \t Price")
    for i,j in cart.items():
        print("\n{0} \t {1} \t {2}".format(i,j,lst[i]))
        sum=sum+(j*lst[i])
    print("\n  \t Total \t: {0}".format(sum))

def signout():
    print("signing out\nHave a nice day!")

def options():
    print("\n Welcome to Consumer module")
    print("\nEnter 1 to view all products in stock")
    print("\nEnter 2 to add products in cart")
    print("\nEnter 3 to view all products in cart")
    print("\nEnter 4 to search for a product in stock")
    print("\nEnter 5 to remove product from cart")
    print("\nEnter 6 to print invoice")
    print("\nEnter 7 to signout of consumer module")

def consumer():
    options()
    choice=int(input("Enter your choice -> "))
    while(True):
        if choice == 1:
            view_products()
        elif choice == 2:
            basket()
        elif choice ==3:
            view_basket()
        elif choice ==4:
            search()
        elif choice == 5:
            remove()
        elif choice== 6 :
            print_invoice()
        elif choice ==7:
            signout()
            break
        else:
            print("Enter a valid option")
        options()
        choice=int(input("Enter your choice-> "))




