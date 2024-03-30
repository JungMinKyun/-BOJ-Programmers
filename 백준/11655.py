# 백준 11655 ROT13

import sys
input = sys.stdin.readline

string = input()
result = ''

for elt in string:
    if elt.islower():
        result += chr((ord(elt) - ord('a') + 13) % 26 + ord('a'))
    elif elt.isupper():
        result += chr((ord(elt) - ord('A') + 13) % 26 + ord('A'))
    else:
        result += elt
    
print(result)