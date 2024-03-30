# 백준 11656 접미사 배열

import sys
input = sys.stdin.readline

result = []
string = input().strip()

for i in range(len(string)):
    result.append(string[i:])

result.sort()

for elt in result:
    print(elt)