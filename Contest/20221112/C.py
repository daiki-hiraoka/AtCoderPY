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

start = 1

path_list = i_row_list(n)


start = [path for path in path_list if 1 in path]
# [path_list.remove(path) for path in path_list if 1 in path]
# print(path_list)
# print(path_list.index(start[1]))

floor = []
def max_floor_func(path: list, now_floor: int, max_floor: int):
    # path_list.remove(path)
    next_floor_index = (path.index(now_floor) + 1) % 2
    next_floor = path[int(next_floor_index)]
    if next_floor > now_floor:
        max_floor = next_floor
    next_path_list = [path for path in path_list if next_floor in path and now_floor not in path]
    if len(next_path_list) == 0:
        return floor.append(max_floor)
    else:
        for path in next_path_list:
            max_floor_func(path, next_floor, max_floor)


if len(start) == 0:
    floor.append(1)
else:
    for path in start:
        max_floor_func(path, 1, 1)
    

print(max(floor))
