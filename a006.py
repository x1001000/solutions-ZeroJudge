while True:
    try:
        line = input()
    except:
        break
    a, b, c = line.split()
    a, b, c = int(a), int(b), int(c)
    D = b**2 - 4*a*c
    if D > 0:
        x1 = (-b + D**0.5) / (2*a)
        x2 = (-b - D**0.5) / (2*a)
        x1, x2 = int(x1), int(x2)
        print('Two different roots x1={} , x2={}'.format(x1,x2))
    elif D==0:
        x = -b / (2*a)
        x = int(x)
        print('Two same roots x={}'.format(x))
    else:
        print('No real root')