import sys
sys.setrecursionlimit(10**7)

n, x, y = map(int, input().split())

e = [[] for _ in range(n+1)]
flag = [False for _ in range(n+1)]
ans = []
stop = False 

for i in range(n-1) :
    u, v = map(int, input().split())
    e[u].append(v)
    e[v].append(u)

def dfs(f, v, p=-1) :
    if v == x :
        ans.append(v)
        return True
    for u in e[v] :
        if u == p :
            continue
        if dfs(f, u, v) :
            ans.append(v)
            return True
    return False

dfs(dfs, y)

print(*ans)

