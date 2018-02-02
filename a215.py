while True:
    try:
        line = input()
    except:
        break
    n, m = line.split()
    n, m = int(n), int(m)
    count = 0             #用來數數
    total = 0             #用來加總
    while True:           #無窮迴圈
        count += 1        #次數增加1
        total += n        #總和增加n
        n += 1            #   n增加1
        if total > m:     #當總和大於m
            break         #跳出迴圈
    print(count)