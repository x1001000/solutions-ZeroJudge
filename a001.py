while True:                     #因為不知測資有幾行，所以用無窮迴圈
    try:                        #try/except是例外處理的語法
        print('hello,', input())#印出hello和輸入字串
    except:                     #直到EOFError發生
        break                   #break無窮迴圈
