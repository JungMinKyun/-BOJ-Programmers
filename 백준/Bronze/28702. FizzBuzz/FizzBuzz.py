# 백준 28702 FizzBuzz

for i in range(3):
    s = input()
    if s not in ['Fizz', 'Buzz', 'FizzBuzz']:
        n = int(s) + (3-i)

print('Fizz'*(n%3==0) + 'Buzz'*(n%5==0) or n)