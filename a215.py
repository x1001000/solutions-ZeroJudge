while True:
    try:
        line = input()
    except:
        break
    n, m = line.split()
    n, m = int(n), int(m)
    count = 0
    sum = 0
    while True:
        count += 1
        sum += n
        n += 1
        if sum > m:
            break
    print(count)