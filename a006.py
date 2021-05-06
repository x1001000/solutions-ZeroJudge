a, b, c = input().split()
a, b, c = int(a), int(b), int(c)
D = b**2 - 4*a*c
if D > 0:
    x1 = (-b + D**0.5) / (2*a)
    x2 = (-b - D**0.5) / (2*a)
    x1 = int(x1)
    x2 = int(x2)
    print(f'Two different roots x1={x1} , x2={x2}')
elif D == 0:
    x = -b // (2*a)
    print(f'Two same roots x={x}')
else:
    print('No real root')
