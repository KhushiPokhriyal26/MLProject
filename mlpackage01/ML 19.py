arr=[i for i in range(1,11) if i%2==0 ]
print(arr)

a=[1,2,3,4,5,6,7,8,9,10]
b=[m*10 for m in range (1,11) if m%3!=0]
print(b)

arr1=['Marry', 'had', 'a', 'littel', 'lamb']
arr1=[(i*10,j) for i,j in enumerate(arr1)]
print(arr1)

arr2=['Marry', 'had', 'a', 'littel', 'lamb']
arr2=[j,k for j,k =len(j) in enumerate(arr)]
print(arr2)