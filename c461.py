while True:
    try:
        a, b, c = map(int, input().split()) # 輸入切成整數a,b,c
        a, b, c = map(bool, [a, b, c])      # a,b,c轉成真假值
    except:                                 # bool(0) return False
        break                               # bool(非0) return True
    impossible = True           # 預設不可能
    if (a and b) == c:
        print('AND')
        impossible = False      # 變成可能
    if (a or  b) == c:
        print('OR')
        impossible = False      # 變成可能
    if (a ^   b) == c:                      # ^為XOR運算子
        print('XOR')
        impossible = False      # 變成可能
    if impossible:              # 當不可能
        print('IMPOSSIBLE')     # 印不可能