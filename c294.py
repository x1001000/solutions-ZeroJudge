while True:
    try:
        three = list(map(int, input().split()))
    except:
        break
    a, b, c = sorted(three)
    print(a,b,c)
    if a + b <= c:
        print('No')
    elif a*a + b*b < c*c:
        print('Obtuse')
    elif a*a + b*b > c*c:
        print('Acute')
    else:
        print('Right')