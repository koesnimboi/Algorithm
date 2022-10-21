from collections import defaultdict
import sys

input = sys.stdin.readline

S, E, Q = input().split()
S = int(S[:2]+S[3:])
E = int(E[:2]+E[3:])
Q = int(Q[:2]+Q[3:])

attend = defaultdict(int)
cnt = 0

while True:
    log = input()
    if len(log) <3:
        break

    time, member = log.split()
    time = int(time[:2] + time[3:])

    if time <= S:
        attend[member] = 1
    elif E <= time <= Q:
        if attend[member] ==1:
            cnt +=1
            attend[member] = 0

print(cnt)