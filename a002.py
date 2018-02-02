while True:
    try:
        line = input()
    except:
        break
    a, b = line.split()     #line切成a和b
    a, b = int(a), int(b)   #a轉整數存入a，b轉整數存入b
    print(a+b)              #印出a+b