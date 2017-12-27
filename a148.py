while True:
    try:
        line = input()
    except:
        break
    strings = line.split()
    integers = [ int(string) for string in strings ]
    average = sum(integers[1:]) / integers[0]
    if average > 59:
        print('no')
    else:
        print('yes')