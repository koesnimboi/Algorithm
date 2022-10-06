import sys

input = sys.stdin.readline

A_num, B_num = map(int, input().split())
A = set(map(int, input().split()))
B = set(map(int, input().split()))

tmp = len(A-B)
tmp2 = len(B-A)
print(tmp+tmp2)