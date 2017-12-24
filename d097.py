while True:
    try:
        line = input()
    except:
        break
    integers = [ int(string) for string in line.split() ]
    n = integers[0]
    test = list(range(1,n))
    for i in range(n-1):
        try:
            test.remove(abs(integers[1:][i]-integers[1:][i+1]))
        except:
            print('Not jolly')
            break
    else:
        print('Jolly')