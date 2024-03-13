# 백준 15278번 에리-카드

import sys
input=sys.stdin.readline

N, K = map(int,input().split())
shared_card = list(map(int, input().split()))
team_card = list(map(int,input().split()))

for _ in range(K):
    max_shared = max(shared_card)
    min_shared = min(shared_card)
    max_team = max(team_card)
    min_team = min(team_card)   
    if max_team >0 and max_shared >0:
        what_is_contact = max(max_shared * max_team, min_team * min_shared)
        if what_is_contact == max_shared * max_team:
            team_card.remove(max_team)
        else:
            team_card.remove(min_team)
    elif max_team <0 and max_shared >0:
        what_is_contact = max(min_shared * min_team, min_shared * max_team)
        if what_is_contact == min_shared * min_team:
            team_card.remove(min_team)
        else:
            team_card.remove(max_team)
    else:
        team_card.remove(min_team)

max_shared = max(shared_card)
min_shared = min(shared_card)
max_team = max(team_card)
min_team = min(team_card)
if max_team >0 and max_shared >0:
    print(max(max_shared * max_team, min_team * min_shared))
elif max_team <0 and max_shared >0:
    print(max(min_shared * min_team, min_shared * max_team))
else:
    print(max(min_team * min_shared, min_team * max_shared))