# 백준 1339번 단어수학

import sys
input = sys.stdin.readline

n = int(input())

alphabets = dict()
for _ in range(n):
    word = list(input().strip())
    for i in range(len(word)):
        if word[i] not in alphabets:
            alphabets[word[i]] = 10 ** (len(word)-i-1)
        else:
            alphabets[word[i]] += 10 ** (len(word)-i-1)
        
alphabets = sorted(alphabets.items(), key=lambda x: x[1], reverse=True)

ans = 0
digits = 9
for key, value in alphabets:
    ans += digits * value
    digits -= 1

print(ans)