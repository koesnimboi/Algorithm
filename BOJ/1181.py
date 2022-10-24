import sys

input = sys.stdin.readline

words_set = set()
N = int(input())

for _ in range(N):
    word = input()
    words_set.add((len(word), word))

sorted_set = sorted(words_set)

for item in sorted_set:
    print(item[1])