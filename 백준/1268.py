# 백준 1268 임시반장 정하기

board = [[0] * 9 for _ in range(5)]

students = []
n = int(input())
for _ in range(n):
    stud = list(map(int, input().split()))
    students.append(stud)
    for i in range(5):
        board[i][stud[i]-1] += 1

ans = [0] * n
for i in range(n):
    for j in range(5):
        elt = students[i][j]
        if board[j][elt-1] > 1:
            ans[i] += board[j][elt-1]-1

print(ans.index(max(ans))+1)

print(ans)