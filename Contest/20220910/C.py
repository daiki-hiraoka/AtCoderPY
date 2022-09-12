N = int(input())
P = list(map(int, input().split()))

max_happy = 0
for i in range(N) :
    happy = 0
    for j in range(N) :
        bl1 = P[j] == (j+i)%N
        bl2 = P[j] == (j+i+1)%N
        bl3 = P[j] == (j+i-1)%N
        if bl1 or bl2 or bl3 :
            happy += 1
    if max_happy < happy :
        max_happy = happy

print(max_happy)