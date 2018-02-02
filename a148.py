while True:               #line.split()是line切成數個字串的一個串列
    try:                  #map(函數,串列)將串列每一項一一代入函數，
        line = input()    #傳回一個map物件
    except:               #list(map物件)將map物件轉成list物件，
        break             #list物件，也就是串列，才支援用中括號存取
    integers = list(map( int, line.split() ))
    average = sum(integers[1:]) / integers[0] #sum()傳回串列總和
    if average > 59:                      #integers[1:]是分數的串列
        print('no')                       #integers[0]是分數的個數
    else:
        print('yes')