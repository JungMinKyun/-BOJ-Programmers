# 백준 5430 AC

import sys
input = sys.stdin.readline

for _ in range(int(input())):
    string = input().rstrip()
    n = int(input())
    arr = input().rstrip()[1:-1].split(',')

    if n == 0:
        arr =[]
    else:
        arr = list(map(int, arr))

    trigger = False
    reverse_count= 0
    for tri in string:
        if tri == 'R':
            reverse_count += 1
        else:
            if not arr:
                print('error')
                trigger = True
                break
            else:
                if reverse_count % 2 == 0:
                    arr.pop(0)
                else:
                    arr.pop()
    
    arr = list(map(str, arr))

    if not trigger:
        if reverse_count % 2 == 1:
            arr.reverse()
        print('['+','.join(arr)+']')