while True:
    try:
        s1, op, s2 = input().split()
    except:
        break
    if op == '+':
        print(int(s1) + int(s2))
    if op == '-':
        print(int(s1) - int(s2))
    if op == '*':
        print(int(s1) * int(s2))
    if op == '/':
        print(int(s1) // int(s2))
