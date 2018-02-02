while True:
    try:
        password = input()
    except:
        break           #for迴圈的變數i從0到5:
    passcode = ''       #password第i位的編碼，減第i+1位的編碼，
    for i in range(6):  #取絕對值，轉成字串，接在passcode後面
        passcode += str(abs(ord(password[i])-ord(password[i+1])))
    print(passcode)