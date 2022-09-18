# input
N = int(input())

A = set()

# 何bit目が1であるか定義しておく
for i in range(60) :
    if N & (1<<i) :
        A.add(i)

k = len(A)
A_list = list(A)
S = set()

for i in range(1<<k) :
    a = 0
    for j in range(k) :
        if(i&(1<<j)) :
            a |= (1<<A_list[j])
    S.add(a)

S = sorted(S)
for var in S :
    print(var)