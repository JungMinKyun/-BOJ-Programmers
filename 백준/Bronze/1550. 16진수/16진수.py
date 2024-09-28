# 백준 1550 16진수

# print(int(input(), 16))

nums = str(input())

con = {'A' : 10, 'B' : 11, 'C' : 12, 'D' : 13, 'E' : 14, 'F' : 15}

ans = 0
for i in range(1,len(nums)+1):
    if nums[-i] in con:
        ans += con[nums[-i]] * (16**(i-1))
    else:
        ans += int(nums[-i]) * (16**(i-1))

print(ans)