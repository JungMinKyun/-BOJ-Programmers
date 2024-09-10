# 백준 1297 TV크기

D, H, W = map(int, input().split())
ratio =  (D**2 / (H**2 + W**2))**0.5

print(int(H*ratio), int(W*ratio))