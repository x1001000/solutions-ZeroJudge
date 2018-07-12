def h(v):                       # 用遞迴函數解遞迴問題
    if H[v] != None:            # 把計算結果都存查
        return H[v]             # 就是 Dynamic Programming 的精神
    if T[v][0] == 0:            # 翻譯成『動態規劃』...
        H[v] = 0                # 可大幅提升遞迴函數的效率
        return H[v]
    h_of_children = []
    for child in T[v][1:]:
        if H[child] == None:
            H[child] = h(child)
        h_of_children.append(H[child])
    H[v] = 1+max(h_of_children)
    return H[v]
T, H, n = [None], [None], int(input())
for _ in range(n):
    T.append(list(map(int, input().split())))
    H.append(None)
for i in range(1,n+1):
    H[i] = h(i)
print(H.index(max(H[1:])))
print(sum(H[1:]))
