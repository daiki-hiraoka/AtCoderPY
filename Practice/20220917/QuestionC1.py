# input
N = int(input())

# 条件に合った集合のsetを定義
S_set = {0}

# N<2^60より60回for文を回す
for d in range(60) :
    if N & (1<<d) : # Nの1のbitの部分で以下の処理を行う
        sz = len(S_set)
        S_list = list(S_set)
        for i in range(sz) :
            S_set.add(S_list[i] | 1<<d) # 集合にある要素全てのdビット目を1にした要素を追加する

S = sorted(S_set)
for val in S :
    print(val)

