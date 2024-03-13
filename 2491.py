# 백준 2491 수열

import sys
input=sys.stdin.readline

N = int(input())
num_list = list(map(int,input().split()))

num_asc = [0] * N
num_dsc = [0] * N

num_asc[0], num_dsc[0] = 1, 1

for i in range(1,N):
	if num_list[i-1] <= num_list[i]:
		num_asc[i] = num_asc[i-1] + 1
	else:
		num_asc[i] = 1

for i in range(1,N):
	if num_list[i-1] >= num_list[i]:
		num_dsc[i] = num_dsc[i-1] + 1
	else:
		num_dsc[i] = 1
		
print(max(max(num_asc), max(num_dsc)))