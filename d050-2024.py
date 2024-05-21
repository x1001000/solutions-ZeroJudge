tw_time = int(input())
# us_time = tw_time - 15
# if us_time >= 0:
#     print(us_time)
# else:
#     print(us_time + 24)
us_time = (tw_time - 15 + 24) % 24
print(us_time)