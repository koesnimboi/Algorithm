import sys
input = sys.stdin.readline

num, count = map(int, input().split())

lst = [i for i in range(1, num+1)]
result = []
seq = count-1

for i in range(num):
    
    if len(lst) > seq:
        result.append(lst.pop(seq))
        seq += count -1
    
    elif len(lst) <= seq:
        seq = seq % len(lst)
        result.append(lst.pop(seq))
        seq += count -1
    
print("<", ', '.join(str(i) for i in result)[:], ">", sep="")