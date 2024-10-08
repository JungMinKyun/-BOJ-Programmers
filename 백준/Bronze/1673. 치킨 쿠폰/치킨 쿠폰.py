# 백준 1673 치킨 쿠폰

while True:
    try:
        n, k = map(int, input().split())

        result = n
        while True:
            result += n//k
            n = n//k + n%k
            if n < k:
                break

        print(result)
        
    except:
        break