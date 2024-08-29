# 백준 1235 학생번호

n = int(input())
nums = [str(input()) for _ in range(n)]

ans = 1

while ans <= 100:
    trigger = False
    temp = set([])
    for num in nums:
        if num[-ans:] not in temp:
            temp.add(num[-ans:])
        else:
            trigger = True
            break
    if trigger:
        ans += 1
    else:
        print(ans)
        break