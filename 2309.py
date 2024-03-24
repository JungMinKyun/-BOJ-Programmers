# 백준 2309 일곱 난쟁이

heights = []
total = 0
for i in range(9):
    height = int(input())
    heights.append(height)
    total += height

target = total - 100

for i in range(8):
    for j in range(i+1, 9):
        if heights[i] + heights[j] == target:
            rm1 = heights[i]
            rm2 = heights[j]

heights.remove(rm1)
heights.remove(rm2)

heights.sort()

for i in range(7):
    print(heights[i])