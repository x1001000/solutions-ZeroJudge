while True:
    try:
        line = input()
    except:
        break
    a, b = line.split()
    a, b = int(a), int(b)
    print(a+b)