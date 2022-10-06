import sys

input = sys.stdin.readline

from collections import defaultdict

N = int(input())
tmp = defaultdict(int)

for _ in range(N):
    tmp[input()] += 1

maxlst = list(key for key, value in tmp.items() if value == max(tmp.values()))
print(sorted(maxlst)[0])