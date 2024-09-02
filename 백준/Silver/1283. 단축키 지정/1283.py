# 백준 1283 단축키 지정

n = int(input())

key_list = []
for _ in range(n):
    keys = list(input().split())
    trigger = False

    for i in range(len(keys)):
        if keys[i][0].upper() not in key_list:
            key_list.append(keys[i][0].upper())
            trigger = True

            keys[i] = '['+keys[i][0]+']'+keys[i][1:]
            print(' '.join(keys))
            break
    
    if not trigger:
        for i in range(len(keys)):
            ckpt = False
            for j in range(len(keys[i])):
                if keys[i][j].upper() not in key_list:
                    key_list.append(keys[i][j].upper())
                    trigger = True
                    ckpt = True
                    
                    keys[i] = keys[i][:j]+'['+keys[i][j]+']'+keys[i][j+1:]
                    print(' '.join(keys))
                    break
            if ckpt:
                break

    if not trigger:
        print(' '.join(keys))



