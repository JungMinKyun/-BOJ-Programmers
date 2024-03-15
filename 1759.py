# 백준 1759 암호 만들기

import sys
input = sys.stdin.readline

vowels = ['a', 'e', 'i', 'o', 'u']

l, c = map(int, input().split())
alphabet = list(input().split())

alphabet.sort()
result = []
def chk(array):
    v_cnt, c_cnt = 0, 0
    for elt in array:
        if elt in vowels:
            v_cnt += 1
        else:
            c_cnt += 1

    if v_cnt >= 1 and c_cnt >=2:
        return True
    else:
        return False

def bt(result):
    if len(result) == l:
        if chk(result):
            print(*result, sep='')
            return
    for i in range(len(result), c):
        if result[-1] < alphabet[i]:
            result.append(alphabet[i])
            bt(result)
            result.pop()

for i in range(c-l+1):
    elt = [alphabet[i]]
    bt(elt)