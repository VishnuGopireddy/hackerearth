'''
Python 2.7
Problem from Hackerearth on Min-Max
'''

length = raw_input()

list_number = map(int, raw_input().split()." ")

total_sum = sum(list_number)
print total_sum - max(list_number),
print total_sum - min(list_number)
