# 백준 4375 1

while True:
    try:
        n = int(input())

        num = int('1' * len(str(n)))
        while num % n:
            num = num * 10 + 1
        
        print(len(str(num)))
    except:
        break