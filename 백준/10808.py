# 백준 10808 알파벳 개수

import sys
input = sys.stdin.readline

result = [0] * 26
string = list(input().strip())

for elt in string:
    result[ord(elt)-ord('a')] += 1

print(*result)