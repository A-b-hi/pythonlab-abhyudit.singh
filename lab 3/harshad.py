
def checkHarshad(n):
    sum = 0
    temp = n
    while temp > 0:
        sum = sum + temp % 10
        temp = temp // 10

    return n % sum == 0

nums=int(input("Enter the number"))
if(checkHarshad(nums)):
    print("Yes")
else:
    print("No")