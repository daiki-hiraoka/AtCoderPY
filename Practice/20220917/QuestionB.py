S = [input().split() for _ in range(10)]

A=C=1e9
B=D=-1e9

A_bool = True
for i in range(10) :

    S_row = "".join(S[i])

    # 変更箇所 max,minを利用する
    if '#' in S_row:
        A = min(A,i+1)
        B = max(B,i+1)
        
    # 変更箇所　max,minを利用する
    if S_row.find('#') != -1 :
        C = min(C,S_row.find('#') + 1)
    D = max(D,S_row.rfind('#') + 1)

    # if c > C :
    #     C = S_row.find('#') + 1

    # if d > D :
    #     D = S_row.rfind('#') + 1

print(A , B)
print(C , D)