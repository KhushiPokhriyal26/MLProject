lst={}
def add_product():
    name=str(input("Enter the name of the product-> "))
    price=eval(input("Enter the price of the product-> "))
    lst[name]=price
    print("{0} product has been added to the stock".format(name))

def update():
    name = str(input("Enter the name of the product-> "))
    if name in lst.keys():
        print("current price is {0}".format(lst[name]))
        price = eval(input("Enter the new price of the product-> "))
        lst[name]=price
        print("updated value is {0}".format(price))
    else:
        print("product is not in the stock")

def remove():
    name = str(input("Enter the name of the product-> "))
    if name in lst.keys():
        del lst[name]
        print("{0} is removed form the stock".format(name))
    else:
        print("the item is not in the list")

def view():
    print("The products are :-\n")
    print("Products \t Prices\n")
    for i,j in lst.items():
        print("-> {0} \t {1}\n".format(i,j))

def logout():
    print("Exiting admin module\n Have a nice day!")

def print_info():
    print("\nWelcome to the admin module")
    print("Enter 1 to add products to the stock")
    print("Enter 2 to update prices in the stock")
    print("Enter 3 to remove products in the stock")
    print("Enter 4 to view all the products in the stock")
    print("Enter 5 to logout of the admin module\n")

def admin():
    print_info()
    choice=int(input("-> "))
    while(True):
        if choice == 1:
            add_product()
        elif choice == 2:
            update()
        elif choice == 3:
            remove()
        elif choice == 4:
            view()
        elif choice == 5:
            logout()
            break
        else:
            print("Enter a valid choice")
        print_info()
        choice=int(input("-> "))


