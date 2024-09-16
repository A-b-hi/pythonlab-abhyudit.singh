n = int(input("enter number : "))

fact = 1
if (n<0):
    print("enter positve number")
elif(n==0):
    print("Factorial of 0 is 1")
else:
    for i in range (1,n+1):
        fact *= i

print("factorial of ",n,"is", fact)