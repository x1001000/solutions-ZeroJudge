#print(eval(input().replace('/', '//')))

s1, op, s2 = input().split()
if op == '+':
    print(int(s1) + int(s2))
if op == '-':
    print(int(s1) - int(s2))
if op == '*':
    print(int(s1) * int(s2))
if op == '/':
    print(int(s1) // int(s2))
