while True:
    try:
        s = input()
    except:
        break
    a,b = s.split()
    a,b = int(a),int(b)
    print(a+b)