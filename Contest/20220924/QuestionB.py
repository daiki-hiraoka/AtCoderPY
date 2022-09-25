X,Y,Z = map(int, input().split())

X_len = abs(X)
Y_len = abs(Y)
Z_len = abs(Z)

goal = 0

if X_len < Y_len or X*Y < 0:
    goal = X_len
elif Z_len < Y_len or Z*Y < 0:
    if X*Z < 0 :
        goal = X_len + 2*Z_len
    else :
        goal = X_len
else :
    goal = -1

print(goal)