import math

def isPrime(n) -> bool:
    if (n <= 1):
        return False
    for i in range(2, int(math.sqrt(n) + 1)):
        if (n % i == 0):
            return False
    return True
    

n = int(input())
if (n == 0):
    print(False)
    exit()
flag = True
while (n > 0):
    if (not isPrime(n)):
        flag = False
        break
    
    n //= 10;
print(flag)

