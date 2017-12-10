while True:
    try:
        number = input()
    except:
        break
    print( int( number[::-1] ) )