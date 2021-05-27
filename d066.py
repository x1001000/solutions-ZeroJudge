h, m = input().split()
h, m = int(h), int(m)
# h = h + m/60
h += m/60
if 7.5 <= h < 17:
    print('At School')
else:
    print('Off School')
