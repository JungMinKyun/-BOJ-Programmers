# 백준 1769 3의 배수

string = str(input())

cnt = 0
while len(string) > 1:
    cnt += 1
    string = str(sum(map(int, string)))

print(cnt)
print("YES" if int(string) % 3 == 0 else "NO")