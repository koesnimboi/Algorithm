# Note1 = list(map(int, input().split())) -> Note1 = set(map(int, input().split()))

import sys

input = sys.stdin.readline

T = int(input())

for _ in range(T):
    Note1_len = int(input())
    Note1 = set(map(int, input().split()))

    Note2_len = int(input())
    Note2 = list(map(int, input().split()))

    for num in Note2:
        if num in Note1:
            print(1)
        else:
            print(0)