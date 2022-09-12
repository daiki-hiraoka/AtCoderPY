A = list(map(int, input().split()))

count = 0
kind = 5

while count < 4 :
    for i in range(count+1, 5) :
        if(A[count] == A[i]) :
            kind -= 1
            break
    count += 1

print(kind)

