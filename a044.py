def f(n):
  if n==1:
    return 2
  if n==2:
    return 4
  return f(n-1) + n*(n-1)//2 + 1
while True:
  try:
    print(f(int(input())))
  except:
    break
