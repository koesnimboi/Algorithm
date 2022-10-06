import sys
import heapq

input = sys.stdin.readline
N = int(input())
data = list(map(int, input().split()))

for _ in range(N-1):
    for num in list(map(int, input().split())):
        if data[0] < num:
            heapq.heappop(data)
            heapq.heappush(data, num)

data[0]