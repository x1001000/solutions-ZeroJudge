now_minute = int(input())
# wait_minute = 25 - now_minute
# if wait_minute >= 0:
#     print(wait_minute)
# else:
#     print(wait_minute + 60)
wait_minute = (25 - now_minute + 60) % 60
print(wait_minute)