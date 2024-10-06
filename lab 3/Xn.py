
def Power(n,x):
    ans=1
    for i in range(1, x+1):
        ans=ans*n
    return ans

print(Power(2,6))