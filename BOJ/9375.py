from collections import defaultdict
import sys

input = sys.stdin.readline

T = int(input())

for _ in range(T):
    N = int(input())
    wear_lst = defaultdict(list)
    cnt = 1

    for _ in range(N):
        wear = input().split()
        wear_lst[wear[1]].append(wear[0])

    for k in wear_lst:
        cnt *= (len(wear_lst[k])+1)

    print(cnt-1)