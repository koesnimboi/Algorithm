from collections import defaultdict
import sys

input = sys.stdin.readline
trees = defaultdict(int)
tree_cnt = 0

while True:
    tree = input().rstrip()
    if not tree:
        break
    trees[tree] += 1
    tree_cnt += 1

tree_lst = sorted(list(trees.keys()))

for t in tree_lst:
    ratio = (trees[t]/tree_cnt)*100
    print('%s %.4f'%(t, ratio))