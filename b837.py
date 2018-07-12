Fib = [0, 1] + [0 for i in range(29)]   #存到第30項
def fib(n):                             #因為第31項超過1000000
    if n > 1:                           #預先算看看可以得知
        x = fib(n-1) if Fib[n-1]==0 else Fib[n-1]
        y = fib(n-2) if Fib[n-2]==0 else Fib[n-2]
        Fib[n] = x+y
    return Fib[n]
fib(30) #算fib(30)使Fib[2]到Fib[30]由預設的0更新為算出來的費氏數
t = int(input())
for i in range(t):              #for迴圈，令i從0到t-1，縮排執行t次
    A, B = sorted(map(int, input().split()))#輸入字串分割轉整數排序
    count = 0                   #走訪前，數量設為0
    for x in Fib:               #走訪費氏數列Fib
        if A <= x <= B:         #當費氏數x介於A和B之間
            print(x)            #印出費氏數x
            count += 1          #數量增加1
    print(count)                #走訪後，印出數量
    if i < t-1:                 #除了最後一圈
        print('------')         #都會印出分隔線
