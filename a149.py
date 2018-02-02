T = int(input())            #讀取T
for _ in range(T):          #重複T次
    line = input()          #讀一行數字
    answer = 1              #設answer為1
    for x in line:          #將一行數字中的每個位數
        answer *= int(x)    #轉整數乘以answer更新answer
    print(answer)           #印answer