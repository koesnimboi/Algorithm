import sys

input = sys.stdin.readline

test_case_num = int(input())

for _ in range(test_case_num):
    doc_num, check_doc = map(int, input().split(' '))
    importance = list(map(int, input().split(' ')))
    
    check_lst = [0 for _ in range(doc_num)]
    check_lst[check_doc] = 1 # check_doc 위치 저장
    
    count = 0
    
    while True: # 무한 루프
        if importance[0] == max(importance):
            count += 1
            
            if check_lst[0] != 1:
                del importance[0]
                del check_lst[0]
            else:
                print(count)
                break
                
        else:
            importance.append(importance[0])
            check_lst.append(check_lst[0])
            
            del importance[0]
            del check_lst[0]