# 백준 1296 팀 이름 정하기

YD = str(input())
ans, res = -1, -1
team_list = []
for _ in range(int(input())):
    
    counts = {'L':0, 'O':0, 'V':0, 'E':0}
    for elt in YD:
        if elt == 'L' or elt == 'O' or elt == 'V' or elt == 'E':
            counts[elt] += 1

    team = str(input())
    for elt in team:
        if elt == 'L' or elt == 'O' or elt == 'V' or elt == 'E':
            counts[elt] += 1

    L, O, V, E = counts['L'], counts['O'], counts['V'], counts['E']
    eq = ((L+O) * (L+V) * (L+E) * (O+V) * (O+E) * (V+E)) % 100
    
    if eq == ans:
        team_list.append(team)
    elif eq > ans:
        team_list = [team]
        ans = eq

team_list.sort()
print(team_list[0])