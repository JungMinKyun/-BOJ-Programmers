# 백준 14916 거스름돈

n = int(input())

if n==1 or n==3:
    print(-1)
else:
    if n%5==3: print(n//5 + 3)
    elif n%5==1: print(n//5 + 2)
    else: print(n//5 + (n%5)//2)