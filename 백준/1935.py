# 백준 1935 후위 표기식2

import sys
input = sys.stdin.readline

n = int(input().strip())
equation = list(input().strip())
operator = {'+', '-', '*', '/'}
idx = [int(input()) for _ in range(n)]

stack = []
for op in equation:
    if 'A' <= op <= 'Z':
        stack.append(idx[ord(op) - 65])
    
    else:
        uop1 = stack.pop()
        uop2 = stack.pop()
        if op == '+':
            stack.append(uop2 + uop1)
        elif op == '-':
            stack.append(uop2 - uop1)
        elif op == '*':
            stack.append(uop2 * uop1)
        elif op == '/':
            stack.append(uop2 / uop1)

print('{:.2f}'.format(stack[0]))