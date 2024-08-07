# 백준 1059 좋은 구간

l = int(input())
s = sorted(list(map(int, input().split()))) 
n = int(input())

if n in s: print(0)
else:
    start, end = 0, 0
    for i in range(l):
        if s[i] < n:
            start = s[i]
        elif s[i] > n and end == 0:
            end = s[i]
    start += 1
    end -= 1
    result = (n-start)*(end-n+1) + (end-n)
    print(result)
    