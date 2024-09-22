# 백준 1408 24

nh, nm, ns = map(int, input().split(':'))
sh, sm, ss = map(int, input().split(':'))

time = (sh*3600 + sm*60 + ss) - (nh*3600 + nm*60 + ns)

if time < 0:
    time += 24*3600

hour, minute, second = time//3600, (time%3600)//60, time%60

print(f'{hour:02d}:{minute:02d}:{second:02d}')