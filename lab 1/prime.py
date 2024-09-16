a=int(input("enter a number"));
c=0;
for i in range(2,a-1,1):
  if(a%i==0):
     c=c+1;
if(c==0):
    print("prime number");
else:
    print("not a prime number");

