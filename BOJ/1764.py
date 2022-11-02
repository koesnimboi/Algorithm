import sys

input = sys.stdin.readline

N, M = map(int, input().split())

Nlst = [input().strip() for _ in range(N)]
Mlst = [input().strip() for _ in range(M)]

intersection = sorted(list(set(Nlst) & set(Mlst)))

print(len(intersection))

for val in intersection:
    print(val)