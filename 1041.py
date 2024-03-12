# 백준 1041 주사위

# A,B,C // A,B,D // A,D,E // A,C,E // F,B,C // F,B,D // F,C,E // F,E,D
# A,D // A,B // A,C // A,E // F,D // F,B // F,C // F,E // B,D // B,C // E,D // E,C
# A,B,C,D,E,F

import sys
input = sys.stdin.readline

n = int(input())
faces = list(map(int, input().split()))
A, B, C, D, E, F = faces[0], faces[1], faces[2], faces[3], faces[4], faces[5]

if n == 1:
    print(sum(faces) - max(faces))

else:
    vertex = min(A+B+C, A+B+D, A+D+E, A+E+C, F+B+C, F+B+D, F+D+E, F+E+C)
    edge = min(A+D, A+B, A+C, A+E, F+D, F+B, F+C, F+E, B+D, B+C, E+D, E+C)
    face = min(faces)

    result = vertex*4 + edge*(4+(n-2)*8) + face*((n-2)*(n-2)+(n-2)*(n-1)*4)

    print(result)