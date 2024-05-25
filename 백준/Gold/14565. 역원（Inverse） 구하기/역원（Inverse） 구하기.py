# 백준 14565 역원(Inverse) 구하기

n, a = map(int, input().split())

div0, div1 = a, n
mod0, mod1 = 1, 0
while div1:
    quo = div0 // div1
    div0, div1 = div1, div0 - div1 * quo
    mod0, mod1 = mod1, mod0 - mod1 * quo

if div0 != 1:
    print(n-a, -1)
else:
    if mod0 <= 0:
        print(n-a, mod0+n)
    else:
        print(n-a, mod0)