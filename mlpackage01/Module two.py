#file Module two.py
print("Top-level in Module two.py")
print("Module two:__name__=",__name__)

#import Module two

if __name__=="__main__":
    print("Module two.py is being run directly")
else:
    print("Module tw.py is being imported into another module")
