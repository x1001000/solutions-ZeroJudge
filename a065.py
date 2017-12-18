while True:
    try:
        password = input()
    except:
        break
    passcode = ''
    for i in range(6):
        passcode += str(abs(ord(password[i])-ord(password[i+1])))
    print(passcode)