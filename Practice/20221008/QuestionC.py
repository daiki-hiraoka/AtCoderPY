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

n = i_input()
a = i_list()
a_even = []
a_odd = []
for i in range(n) :
    if a[i] % 2 == 0 :
        a_even.append(a[i])
    else :
        a_odd.append(a[i])

a_even.sort()
a_odd.sort()
sum1 = 0
sum2 = 0
if len(a_even) > 1 :
    sum1 = a_even.pop() + a_even.pop()
if len(a_odd) > 1 :
    sum2 = a_odd.pop() + a_odd.pop()

ans = max(sum1,sum2)
if ans == 0 :
    ans = -1
print(ans)