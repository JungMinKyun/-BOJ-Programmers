# 백준 2447 별 찍기 - 10

stars = ['***', '* *', '***']

def staring(k, n, stars):
    if k == n:
        return stars
    new_stars = []
    for i in range(k):
        new_stars.append(stars[i]*3)
    for i in range(k):
        new_stars.append(stars[i] + ' ' * k + stars[i])
    for i in range(k):
        new_stars.append(stars[i]*3)
    
    return staring(k*3, n, new_stars)

total_stars = staring(3, int(input()), stars)

for star in total_stars:
    print(star)