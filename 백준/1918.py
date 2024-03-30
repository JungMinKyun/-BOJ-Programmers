# 백준 1918 후위 표기식

import sys
input = sys.stdin.readline

equation = input().strip()
result = ''
stack = []

for op in equation:
    if 'A' <= op <= 'Z':
            result = result + op
            
    else:
        if op == '(':
            stack.append(op)
        elif op == '*' or op == '/':
            while stack and (stack[-1] == '*' or stack[-1] == '/'):
                 result = result + stack.pop()
            stack.append(op)
        elif op == '+' or op == '-':
            while stack and stack[-1] != '(':
                 result = result + stack.pop()
            stack.append(op)
        else:
            while stack and stack[-1] != '(':
                 result = result + stack.pop()
            stack.pop()

while stack:
    result = result + stack.pop()

print(result)