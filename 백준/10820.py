# 백준 10820 문자열 분석

import sys
input = sys.stdin.readline

while True:
    string = input().rstrip('\n')

    if not string:
        break

    low, up, num, space = 0, 0, 0, 0

    for elt in string:
        if elt == ' ':
            space += 1
        elif elt.isalpha():
            if ord(elt) <= ord('Z'):
                up += 1
            else:
                low += 1
        else:
            num += 1

    print(low, up, num, space)