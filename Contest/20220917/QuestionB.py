S = [input().split() for _ in range(10)]

A=C=1e9
B=D=-1e9

A_bool = True
for i in range(10) :

    S_row = "".join(S[i])

    if '#' in S_row:
        B = i + 1
        if A_bool :
            A = i + 1
            A_bool = False

    c = S_row.find('#') + 1
    d = S_row.rfind('#') - 1

    if c > C :
        C = S_row.find('#') + 1

    if d > D :
        D = S_row.rfind('#') + 1

print(A , B)
print(C , D)