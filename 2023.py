# 백준 2023 신기한 소수

import sys
n = int(input())

def is_prime(num):
    for i in range(2, int(num**0.5)+1):
        if num % i == 0:
            return False
    return True

def BT(num):
    if len(str(num)) == n:
        print(num)
        return
    else:
        for i in range(1, 10):
            if i % 2 == 0:
                continue
            else:
                if is_prime(int(str(num)+str(i))):
                    BT(int(str(num)+str(i)))

for num in [2, 3, 5, 7]:
    BT(num)