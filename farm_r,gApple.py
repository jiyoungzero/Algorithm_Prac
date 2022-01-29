import math
import sys

r,g = map(int, sys.stdin.readline().split())

def gcd(a, b): # 최대공배수 찾기
    if b == 0:
        return a
    else:
        return gcd(b, a % b)

lst = []
temp = gcd(r, g)
sqrt_temp = math.sqrt(temp)  

for i in range(1, int(sqrt_temp)+1): # 최대공배수의 루트 값까지만 찾기
    if temp % i == 0:
        lst.append(i)
        if temp // i == i:
            continue
        lst.append(temp // i)
lst.sort()
for i in lst:
    print(i, r // i, g // i)