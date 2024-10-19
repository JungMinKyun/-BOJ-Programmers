# 백준 1919 애너그램 만들기

text1 = input().strip()
text2 = input().strip()

alp1 = [0]*26
alp2 = [0]*26

ans = 0

for i in range(len(text1)):
    alp1[ord(text1[i])-97] += 1
for i in range(len(text2)):
    alp2[ord(text2[i])-97] += 1

for i in range(26):
    ans += abs(alp1[i]-alp2[i])

print(ans)