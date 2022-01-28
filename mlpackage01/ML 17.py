arr=['Marry', 'had', 'a', 'little', 'lamb']
print(enumerate(arr))

print(list(enumerate(arr)))
print(tuple(enumerate(arr)))

arr1=[(0,'Marry'), (1,'had'), (2,'a'), (3,'little'), (4,'lamb')]
print(list(enumerate(arr1)))


for i,j in enumerate(arr):
    print(i, "=" ,j)

for a in enumerate(arr):
    print("a=" , a)
