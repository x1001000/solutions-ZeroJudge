while True:
    try:
        line = input()
    except:
        break
    integers = [ int(string) for string in line.split() ]
    average = sum(integers[1:])/integers[0]
    if average > 59:
        print('no')
    else:
        print('yes')