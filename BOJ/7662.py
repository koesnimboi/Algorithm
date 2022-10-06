import heapq
import sys

input = sys.stdin.readline

T = int(input())

for _ in range(T):
    k = int(input())
    visited = [False] * 1000001
    min_heap, max_heap = [], []

    for i in range(k):
        operator, num = input().split()
        if operator == 'I':
            heapq.heappush(min_heap, (int(num), i))
            heapq.heappush(max_heap, (-int(num), i))
            visited[i] = True
        else:
            if num == '-1':
                while min_heap and not visited[min_heap[0][1]]:
                    heapq.heappop(min_heap)
                if min_heap:
                    visited[min_heap[0][1]] = False
                    heapq.heappop(min_heap)

            if num == '1':
                while max_heap and not visited[max_heap[0][1]]:
                    heapq.heappop(max_heap)
                if max_heap:
                    visited[max_heap[0][1]] = False
                    heapq.heappop(max_heap)

    if True not in visited:
        print("EMPTY")
    else:
        while min_heap and not visited[min_heap[0][1]]:
            heapq.heappop(min_heap)
        while max_heap and not visited[max_heap[0][1]]:
            heapq.heappop(max_heap)

        print(-max_heap[0][0], min_heap[0][0])