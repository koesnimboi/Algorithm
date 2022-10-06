import sys

N, M = map(int, sys.stdin.readline().split())

S = set([input() for _ in range(N)])

cnt = 0

for _ in range(M):
    word = input()
    if word in S:
        cnt += 1
        
print(cnt)