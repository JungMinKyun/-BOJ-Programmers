# 백준 4796번 캠핑

case_num = 0
while True:
    case_num += 1
    L, P, V = map(int, input().split())
    if L == P == V == 0:
        break  
    ans = 0
    ans += (V//P) * L
    ans += min((V%P), L)
    print('Case {0}: {1}'.format(case_num, ans))