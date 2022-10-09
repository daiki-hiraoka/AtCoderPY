from pickle import FALSE, TRUE
import sys, re
from math import ceil, floor, sqrt, pi, factorial, gcd
from copy import deepcopy
from collections import Counter, deque
from heapq import heapify, heappop, heappush
from itertools import accumulate, product, combinations, combinations_with_replacement
from bisect import bisect, bisect_left, bisect_right
from functools import reduce
from decimal import Decimal, getcontext
def i_input(): return int(input())
def i_map(): return map(int, input().split())
def i_list(): return list(i_map())
def i_row(N): return [i_input() for _ in range(N)]
def i_row_list(N): return [i_list() for _ in range(N)]
def s_input(): return input()
def s_map(): return input().split()
def s_list(): return list(s_map())
def s_row(N): return [s_input() for _ in range(N)]
def s_row_str(N): return [s_list() for _ in range(N)]
def s_row_list(N): return [list(s_input()) for _ in range(N)]
def lcm(a, b): return a * b // gcd(a, b)
sys.setrecursionlimit(10 ** 6)
INF = float('inf')
MOD = 10 ** 9 + 7

n,m = i_map()
k = i_row_list(m)

l = [set() for i in range(n)]

for i in range(n) :
    s = set()
    for j in range(m) :
        k_loss = k[j]
        loss = k_loss.pop(0)
        if i+1 in k_loss :
            k_loss.insert(0,loss)
            for t in range(1,k[j][0]+1) :
                l[i].add(k[j][t])
        else :
            k_loss.insert(0,loss)
            continue

bool = False

for i in range(1,n) :
    if l[0] == l[i] :
        bool = True
    else :
        bool = False
        break


if bool :
    print('Yes')
else :
    print('No')