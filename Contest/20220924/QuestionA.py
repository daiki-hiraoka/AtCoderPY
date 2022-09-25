A,B = map(int, input().split())

A_set = set()
B_set = set()

list = list((4,2,1))

for sc in list :
    if A - sc >= 0:
        A_set.add(sc)
        A -= sc
    if B - sc >= 0:
        B_set.add(sc)
        B -= sc

A_set |= B_set

score = 0
for i in range(len(A_set)) :
    score += A_set.pop()

print(score)