while True:
    try:
        n = int(input())
    except:
        break
    print((85-n)%60)