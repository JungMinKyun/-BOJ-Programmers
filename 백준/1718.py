# 백준 1718 암호

target = input()
key = input()

res = ''
for i in range(len(target)):
    if target[i] == ' ':
        res += ' '
    else:
        res += chr((ord(target[i]) - ord(key[i%len(key)]) - 1)%26 + 97)

print(res)