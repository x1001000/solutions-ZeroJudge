while True:
    n = int(input())
    if n == 0:          #輸入到測資最後一行0
        break           #就跳出while迴圈
    for i in range(1,n):      #令i為1到n-1
        if i%7 != 0:          #若i不為7的倍數
            print(i,end=' ')  #印出i，end參數預設值為換行，改為空格
    print()             #如範例所示，一行輸入對應一行輸出，故要換行