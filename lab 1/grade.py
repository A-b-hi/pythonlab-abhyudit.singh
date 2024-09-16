n=int(input("enter a number :"))
Rnm=0
while n!=0 :
    y=n%10
    n=int(n/10)
    Rnm=Rnm*10+y
print(Rnm)
if(Rnm==n): print("it is a palindrome")
if(Rnm!=n): print("it is not a palindrome")