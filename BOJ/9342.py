import sys
import re

input = sys.stdin.readline
p = re.compile('^[A-F]?A+F+C+[A-F]?$')

for _ in range(int(input())):
    print('Good' if p.match(input())==None else 'Infected!')