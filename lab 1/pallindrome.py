a=int(input("enter a number"));
rev=0;
t=a;
while t>0:
     m=t%10;
     rev=rev*10+m;
     t=t//10;
if(a==rev):
     print("pallindrome number");
else:
    print("not a pallindrome number");
     
   