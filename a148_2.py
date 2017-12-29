while True:
    try:
        line = input()
    except:
        break
    integers = line.split()
    integers = map(int,integers)
    integers = list(integers)
    average = sum(integers[1:]) / integers[0]
    if average > 59:
        print('no')
    else:
        print('yes')