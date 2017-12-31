while True:
    try:
        line = input()
    except:
        break
    n, m = line.split()
    n, m = int(n), int(m)
    count = 0
    total = 0
    while True:
        count += 1
        total += n
        n += 1
        if total > m:
            break
    print(count)