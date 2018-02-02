while True:
    try:
        line = input()
    except:
        break
    M, D = line.split()
    M, D = int(M), int(D)
    S = (M*2+D)%3
    if S == 0:          #如果S等於0，進入第10行，否則跳到第11行
        print('普通')
    elif S == 1:        #那如果S等於1，進入第12行，否則跳到第13行
        print('吉')
    elif S == 2:        #那如果S等於2，進入第14行，if可搭配多個elif
        print('大吉')