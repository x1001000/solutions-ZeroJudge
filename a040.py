def is_Armstrong_number(n):
    S = str(n)
    L = len(S)
    x = 0
    for i in S:
        x += int(i)**L
    if x == n:
        return True
    else:
        return False

while True:
    try:
        line = input()
    except:
        break
    n, m = line.split()
    n, m = int(n), int(m)
    no_Armstrong_number = True
    for i in range(n,m+1):
        if is_Armstrong_number(i):
            print(i,end=' ')
            no_Armstrong_number = False
    if no_Armstrong_number:
        print('none',end='')
    print()