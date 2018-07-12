N = int(input())
W = list(map(int, input().split()))
f = list(map(int, input().split()))
Minimum = dict()

def minimum(stack):
    if Minimum.get(str(stack)):
        return Minimum[str(stack)]
    if len(stack) == 2:
        Minimum[str(stack)] = min(f[stack[0]]*W[stack[1]],f[stack[1]]*W[stack[0]])
        return Minimum[str(stack)]
    minimums = []
    for i in range(len(stack)):
        below = stack[:i]+stack[i+1:]
        extra = 0
        for j in below:
            extra += f[j]*W[stack[i]]
        min_below = Minimum.get(str(below), minimum(below))
        minimums.append(min_below+extra)
    Minimum[str(stack)] = min(minimums)
    return Minimum[str(stack)]

print(minimum(list(range(N))))
