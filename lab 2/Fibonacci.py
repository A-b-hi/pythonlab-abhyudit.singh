n = int(input("enter no. of terms : "))

a , b = 0 , 1
count = 0

if (n<=0):
    print("enter positive number")
elif(n==1):
    print(a)
else:
    print("Fiboacci series : ")
    while(count<n):
        print(a)
        c = a+b
        a = b
        b = c
        count += 1