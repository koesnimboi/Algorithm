import sys
from collections import defaultdict

input = sys.stdin.readline
file_dict = defaultdict(int)

for _ in range(int(input())):
    file = input()
    file_dict[file[file.find('.')+1:]] += 1

file_dict = sorted(file_dict.items())

for key, value in file_dict:
    print(key.rstrip(), value)