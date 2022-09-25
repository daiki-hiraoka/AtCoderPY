n, x, y = map(int, input().split())

e = [[] for _ in range(200010)]
flag = [False for _ in range(200010)]
ans = []
stop = False 

for i in range(n-1) :
    u, v = map(int, input().split())
    e[u].append(v)
    e[v].append(u)

def dfs(k, to) :
    global stop
    if not stop :
        ans.append(k)
    if k == to :
        stop = True

    flag[k] = True
    sz = len(e[k])

    for i in range(sz) :
        if e[k][i] == to :
            ans.append(e[k][i])
            stop = True
            break
        if not flag[e[k][i]] :
            dfs(e[k][i], to)
    
    if not stop :
        ans.pop()

dfs(x,y)

print(*ans)

