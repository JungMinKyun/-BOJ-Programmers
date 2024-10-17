# 백준 1871 좋은 자동차 번호판

n = int(input())
for _ in range(n):
    alp, num = input().split('-')
    
    val1 = 26**2*(ord(alp[0])-ord('A')) + 26*(ord(alp[1])-ord('A')) + (ord(alp[2])-ord('A'))
    val2 = int(num)

    if abs(val1-val2) <= 100:
        print('nice')
    else:
        print('not nice')