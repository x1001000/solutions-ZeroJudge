while True:
    try:
        year = int(input())
    except:
        break
    if (year%4==0 and year%100!=0) or year%400==0:
        print('閏年')
    else:
        print('平年')