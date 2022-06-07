while True:
    try:
        n, k = input().split()
    except:
        break
    n, k = int(n), int(k)
    if n == 0:
        print('Ok!')
    elif k == 0:
        print('Impossib1e!')
    elif n < k:
        print('Impossib1e!')
    elif n % k:
        print('Impossib1e!')
    else:
        print('Ok!')
