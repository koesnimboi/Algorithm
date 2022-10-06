import sys
from collections import defaultdict

input = sys.stdin.readline

N = int(input())
part_dict = defaultdict(int)

for i in range(2*N-1):
    if i > N-1:
        part_dict[input()] -= 1
    else:
        part_dict[input()] += 1

tmp = list(part_dict.values())
tmp2 = list(part_dict.keys())
idx = tmp.index(1)

nonfinish = tmp2[idx]

print(nonfinish)