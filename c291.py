while True:
  try:
    N=int(input())
  except:
    break
  X=[int(x) for x in input().split()]
  Y=[True for _ in range(N)]
  group=0
  for x in X:
    if Y[x]:
      Y[x]=False
      friend=X[x]
      while not friend==x:
        Y[friend]=False
        friend=X[friend]
      group+=1
  print(group)
'''
輸入字串轉成整數存入N
發生EOF時跳出迴圈
X是好友編號的list
Y是待追蹤狀態的list
group是小群體個數
對於X的每一項x
若待追蹤則進入追蹤流程
待追蹤狀態改成False
追蹤回x就跳出while迴圈然後小群體個數加一
輸出小群體個數
'''
