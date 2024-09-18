# 백준 1357 뒤집힌 덧셈

str1, str2 = map(str, input().split())
eqa = int(str1[::-1]) + int(str2[::-1])
print(int(str(eqa)[::-1]))