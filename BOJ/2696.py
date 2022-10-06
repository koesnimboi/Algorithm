import heapq
import sys

input = sys.stdin.readline

def check(data):
    left, right = [], []
    middle = data[0]
    result = [middle]
    for idx, val in enumerate(data[1:], 1):
        if val > middle: # 중앙값 보다 크면
            heapq.heappush(right, val) # 최소 힙인 오른쪽 힙에 삽입
        else: # 중앙값 보다 작으면
            heapq.heappush(left, -val) # 최대 힙인 왼쪽 힙에 삽입
        if idx % 2 == 0:  # 삽입이 2번 이루어질 때마다 길이를 비교
            if len(left) < len(right):  # 오른쪽 힙이 왼쪽 힙보다 길이가 길다면
                heapq.heappush(left, -middle)  # 기존의 중앙값은 왼쪽 힙에 삽입
                middle = heapq.heappop(right)  # 오른쪽 힙의 값을 중앙값으로 이용
            elif len(left) > len(right):  # 왼쪽 힙이 오른쪽 힙보다 길이가 길다면
                heapq.heappush(right, middle)  # 기존의 중앙값을 오른쪽 힙에 삽입
                middle = -heapq.heappop(left)  # 왼쪽 힙의 값을 중앙값으로 이용
            result.append(middle)

    print(len(result))

    for i in range(len(result)):
        if (i + 1) != 1 and (i + 1) % 10 == 1:
            print()
        print(result[i], end=' ')
    print()


t = int(input().rstrip())

for _ in range(t):
    m = int(input())
    data = []

    if m % 10 == 0:
        for _ in range(m // 10):
            data.extend(list(map(int, input().rstrip().split())))
    else:
        for _ in range(m // 10 + 1):
            data.extend(list(map(int, input().rstrip().split())))

    check(data)