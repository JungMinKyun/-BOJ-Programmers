# 백준 2812번 크게 만들기

import sys
input = sys.stdin.readline

n, k = map(int, input().split())
nums = list(input().rstrip())

# 시간초과 발생 코드
# result = []

# while k > 0:
#     temp_max = int(max(nums[:k+1]))
#     result.append(temp_max)
#     for i in range(k+1):
#         if int(nums[i]) == temp_max:
#             max_idx = i
#             break
#     k -= max_idx
#     nums = nums[max_idx+1:]

# result.extend(nums)

# print(*result, sep='')

# 로직은 동일하나, 복사해서 생성하는 시간 등 구조가 최적화된 코드

result = []
for num in nums:
    while result and k > 0:
        if result[-1] < num:
            result.pop()
            k -= 1
        else:
            break
    result.append(num)

if k > 0:
    print(*result[:-k], sep = '')
else:
    print(*result, sep='')



