def is_Armstrong_number(n):
    x = 0
    for s in str(n):
        x += int(s)**len(str(n))
    return True if x == n else False

while True:
    try:
        n, m = map(int, input().split())
    except:
        break
    there_is_none = True
    for i in range(n,m+1):
        if is_Armstrong_number(i):
            there_is_none = False
            print(i,end=' ')
    if there_is_none:
        print('none',end='')
    print()
