#file Module one.py
print("Top-level in Module one.py")
print("Module one :__name__", __name__)

def func():
    print("func() in Module one.py")

if __name__=="__main__" :
    print("Module one.py is being run directly")
else:
    print("Module one.py is being imported to another module")