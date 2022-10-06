from collections import deque
import sys

input = sys.stdin.readline
N = deque([i for i in range(1, int(input())+1)])

while len(N) > 1:
    del N[0]
    N.append(N[0])
    del N[0]
    
print(N[0])