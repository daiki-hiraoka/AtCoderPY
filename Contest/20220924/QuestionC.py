N,X,Y = map(int, input().split())

U = set()
for i in range(N-1) :
    U_1, U_2 = map(int, input().split())
    U.add({U_1,U_2})
