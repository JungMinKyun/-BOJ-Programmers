# 백준 9237 이장님 초대

n = int(input())
nums = list(map(int, input().split()))
nums.sort(reverse=True)

ans = 0
for i in range(n):
    ans = max(ans, nums[i]+i+2)

print(ans)