# With brute force, not using Bit Manipulation
import math
def dectobin(n):
    if n == 0:
        return "0"
    ans = ""
    while(n > 0):
        dg = n % 2
        ans += str(dg)
        n = n // 2
    return ans[::-1]

def magicnumber(n):

    bin = reversed(dectobin(n))
    sum = 0
    p = 1
    for dg in bin:
        sum += int(dg) * math.pow(5,p)
        p +=1
    return int(sum)


print(magicnumber(6))

'''
# Using Bit Manipulation
def magicnumber2(n):
    pow = 5
    sum = 0
    while(n > 0):
        last = n & 1 #(Gives the last digit of the binary representation of n)
        sum += last * pow
        n = n >> 1
        pow = pow * 5
    return sum

print(magicnumber2(6))
'''

