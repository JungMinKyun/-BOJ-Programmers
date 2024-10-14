# 백준 1864 문어 숫자

import sys
input = sys.stdin.readline

oct_dict = {'-': 0, '\\': 1, '(': 2, '@': 3, '?': 4, '>': 5, '&': 6, '%': 7, '/': -1}

while True:
    letter = input().strip()
    if letter == '#':
        break
    else:
        result = 0
        for i in range(len(letter)):
            result += oct_dict[letter[i]]*(8**(len(letter)-1-i))
        
        print(result)
