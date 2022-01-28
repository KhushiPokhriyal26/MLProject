num=int(input("Enter number for prime number testing:"))

for a in range(2,num):
    if num%a==0:
        print(num, "is not a prime number")
        break
else:
    print(num, "is a prime number")
