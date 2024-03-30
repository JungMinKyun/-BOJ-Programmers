# 백준 2089 -2진수

# 1, -2, 4, 0, 16, -32, ...

n = int(input())
ans = ''

if n==0:
    print(0)
else:
    while n != 0:
        if n % (-2) != 0:
            n = n//(-2) + 1
            ans += '1'
        else:
            n = n//(-2)
            ans += '0'

    print(ans[::-1])