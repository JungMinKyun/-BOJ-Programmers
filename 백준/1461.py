# 백준 1461 도서관

import sys
input = sys.stdin.readline

n, m = map(int, input().split())
books = list(map(int, input().split()))
books.sort()

posit = []
negat = []
max_book = 0
for book in books:
    if book > 0:
        posit.insert(0, book)
        max_book = max(max_book, abs(book))
    else:
        negat.append(book)
        max_book = max(max_book, abs(book))

result = 0
if posit:
    for i in range(0, len(posit), m):
        result += posit[i]*2
if negat:
    for i in range(0, len(negat), m):
        result += abs(negat[i])*2

print(result - max_book)