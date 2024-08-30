# 백준 1205 등수 구하기

n, score, p = map(int, input().split())
if n == 0:
    print(1)
else:
    nums = list(map(int, input().split()))

    if n == p and nums[-1] >= score:
        print(-1)
    else:    
        ans = n + 1
        for i in range(min(n, p)):
            if nums[i] <= score:
                ans = i + 1
                break

        print(ans)