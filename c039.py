while True:
    try:
        i, j = map(int, input().split())
    except:
        break
    I, J = (j, i) if i > j else (i, j)
    cycles = []
    for x in range(I, J+1):
        #print(f'Cycle of {x} is [{x}', end=' ')
        cycle = 1
        while x != 1:
            if x%2 == 0:
                x = x//2
                #print(x, end=' ')
                cycle = cycle+1
            else:
                x = x*3+1
                #print(x, end=' ')
                cycle = cycle+1
        #print('], so its cycle length is', cycle)
        cycles.append(cycle)
    print(i, j, max(cycles))
