while True:
  try:
    a,b,N=input().split()
    a,b,N=int(a),int(b),int(N)
    answer=str(10**N*a//b)
    n=len(answer)
    if N>=n:
      print('0.'+'0'*(N-n)+answer[-N:])
    else:
      print(answer[:-N]+'.'+answer[-N:])
  except:
    break
