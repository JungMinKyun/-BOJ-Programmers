# 백준 1284 집 주소

while True:
    temp = str(input())
    if temp == '0':
        break
    else:
        ans = len(temp) + 1
        for elt in temp:
            if elt == '0': ans += 4
            elif elt == '1': ans += 2
            else: ans += 3
        
        print(ans)
