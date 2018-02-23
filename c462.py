while True:
    try:
        k, s = int(input()), input()
    except:
        break
    count = 0
    counts = []
    pre = s[0].isupper()    #迴圈前，先記s[0]狀態，大寫為真小寫為假
    for c in s:             #迴圈中，左至右走訪s，小寫為真大寫為假
        if pre ^ c.islower():   #當互斥，互斥就是一真一假
            pre = c.islower()   #更新pre，小寫為真大寫為假
            counts.append(count)#狀態連續次數count存入counts
            count = 1           #狀態連續次數設為1
        else:                   #否則，
            count += 1          #狀態連續次數增加1
    counts.append(count)    #迴圈後，狀態連續次數count存入counts
    answer, length = 0, 0
    #print(counts)
    for i in range(1,len(counts)):  #從位置1走訪counts
        if counts[i] == k:          #當狀態連續次數為k
            length += k             #交錯字串長度增加k
            if counts[i-1] > k:     #若前次狀態連續次數大於k
                length += k         #交錯字串長度再增加k
        else:                       #當狀態連續次數不為k
            if counts[i] > k:       #若狀態連續次數大於k
                length += k         #交錯字串長度再增加k
            answer = max(answer,length) #留下最大的交錯字串長度
            length = 0
    print(max(answer,length))       #印出最大的交錯字串長度