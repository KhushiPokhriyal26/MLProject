#First Method
alpha=input("Enter alphabet to search:")

searchstatus= False
for ch in "ABCDE":
    if (ch==alpha):
        searchstatus=True
        break

if searchstatus==True:
    print(alpha, "found in the given word")
else:
    print(alpha, "not found in the given word")


#Second Method
alpha = input("Enter alphabet to search:")

for ch in "ABCDE":
    if (ch == alpha):
        print(alpha, "found in the given word")
        break
else:
    print(alpha, "not found in the given word")
