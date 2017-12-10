while True:
    try:
        string = input()
    except:
        break
    if string == string[::-1]:
        print('yes')
    else:
        print('no')