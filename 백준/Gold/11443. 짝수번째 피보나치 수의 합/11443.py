# 백준 11443 짝수번째 피보나치 수의 합

import sys
input = sys.stdin.readline

mod = 1000000007

# 분할정복을 이용한 피보나치 찾기 (행렬곱셈)
def mul_mat(a_mat,b_mat):
    temp_mat = [[0, 0], [0, 0]]
    for i in range(2):
        for j in range(2):
            for k in range(2):
                temp_mat[i][j] += a_mat[i][k] * b_mat[k][j] % mod
    return temp_mat
    

def fibo(mat, n):
    if n == 1: return mat
    else:
        if n % 2 == 0:
            half = fibo(mat, n//2)
            return mul_mat(half, half)
        else:
            half = fibo(mat, n//2)
            return mul_mat(mul_mat(half, half), mat)
        
n = int(input())
ans = fibo([[1, 1], [1, 0]], n)
if n % 2 == 0:
    print((ans[0][0] - 1) % mod)
else:
    print((ans[0][1] - 1) % mod)