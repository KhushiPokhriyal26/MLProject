#Question 1
#arr=["Mary", "had", "a", "a", "little", "lamb"]

#Question 2
arr=[['A','Mary'], ['B','had'], ['C','a']]

for i,j in enumerate(arr):
    print(i, "=", type(i))
    print(j, "=", type(j))

for i,[j,k] in enumerate(arr):
    print(i, "=", type(i))
    print(j, "=", type(j))
    print(k, "=", type(k))

for i in enumerate(arr):
    print(i)
