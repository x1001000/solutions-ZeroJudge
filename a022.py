while True:
    try:                    #字串[start:stop:step]為字串的片段
        line = input()      # step省略不寫就是1，若step為負數，
    except:                 #start省略不寫就是從最右邊，
        break               # stop省略不寫就是到最左邊
    if line == line[::-1]:  #若line為迴文
        print('yes')
    else:
        print('no')