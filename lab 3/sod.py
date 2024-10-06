
def getSum(n): 
   
    sum = 0
    for i in str(n):  
      sum += int(i)       
    return sum
  
n=int(input("Enter the req. number"))

print(getSum(n))