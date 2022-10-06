import sys

input = sys.stdin.readline

month, day = map(int, input().split())

days = 0
days_lst = ['SUN', 'MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT']
days_lst2 = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

for i in range(0, month-1):
    days += days_lst2[i]

days = (days+day)%7

print(days_lst[days])