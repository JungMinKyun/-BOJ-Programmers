# 백준 1406 에디터

import sys
input = sys.stdin.readline

# stack = list(input().rstrip())
# cursor = len(stack)

# for _ in range(int(input())):
#     command = list(input().split())
#     if command[0] == 'P':
#         stack.insert(cursor, command[-1])
#         cursor += 1
#     elif command[0] == 'L':
#         cursor = max(0, cursor-1)
#     elif command[0] == 'D':
#         cursor = min(len(stack), cursor+1)
#     elif command[0] == 'B':
#         if cursor > 0:
#             cursor -= 1
#             stack.remove(stack[cursor])

# print(*stack, sep='')

stack1 = list(input().rstrip())
stack2 = []

for _ in range(int(input())):
    command = list(input().split())
    if command[0] == 'L':
        if stack1:
            stack2.append(stack1.pop())
    elif command[0] == 'D':
        if stack2:
            stack1.append(stack2.pop())
    elif command[0] == 'B':
        if stack1:
            stack1.pop()
    else:
        stack1.append(command[1])

stack1.extend(reversed(stack2))
print(*stack1, sep='')