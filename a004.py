while True:
    try:
        year = int(input()) #輸入轉整數存入year
    except:
        break  #⬇︎西元年被4整除且不被100整除，或被400整除者即為閏年
    if (year%4==0 and year%100!=0) or year%400==0:
        print('閏年')
    else:
        print('平年')