N = int(input())

S = set()

for i in reversed(range((1<<60)-1)) :
    i &= N
    S.add(i)

S = sorted(S)
for val in S :
    print(S)