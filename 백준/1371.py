# 백준 1371 가장 많은 글자

import sys
input = sys.stdin.read

string = input()
arr = [0]*26 

for line in string:
    if line.islower():
        arr[ord(line)-97] += 1
for i in range(26): 
    if arr[i] == max(arr):
        print(chr(97+i), end='')