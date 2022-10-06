import sys

input = sys.stdin.readline

num = int(input())
balloon_lst = [i+1 for i in range(num)]
balloon_with_num = list(map(int, input().split(' ')))
answer = []
seq = 0

while True:
    answer.append(balloon_lst[seq])
    balloon_lst.pop(seq)
    step = balloon_with_num.pop(seq)
    
    if not balloon_lst:
        break
        
    if step > 0:
        seq = (seq + step - 1 )% len(balloon_lst)
    else:
        seq = (seq + step)% len(balloon_lst)

for i in answer:
    print(i)