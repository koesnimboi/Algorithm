import sys

input = sys.stdin.readline

while True:
    try:
        n1, n2 = input().split()
        
        idx = 0
        whether = False

        for letter in n2:
            if n1[idx] == letter:
                idx += 1
            if idx == len(n1):
                whether = True
                break
        
        if whether:
            print('Yes')
        else:
            print('No')
    except:
        break