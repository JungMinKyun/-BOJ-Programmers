# 백준 1076 저항

col_list = ['black', 'brown', 'red', 'orange', 'yellow', 'green',
            'blue', 'violet', 'grey', 'white']

ans = ''
for _ in range(2):
    temp = str(input())
    ans = ans + str(col_list.index(temp))

temp = str(input())
ans = int(ans) * 10 ** (col_list.index(temp))

print(ans)