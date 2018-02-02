while True:               #因為不知測資有幾行，所以用無窮迴圈
    try:                  #try/except是例外處理，當try失敗
        line = input()    #若成功輸入一行字串，就存入變數line
    except:               #就會進入except
        break             #break會跳出while迴圈
    print('hello,', line) #然後印出字串'hello'和變數line