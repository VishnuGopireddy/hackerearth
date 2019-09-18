# python 2.6
#Program on Monk and Philosopher's Stone from HACKER EARTH
a = int(raw_input())
values = map(int,raw_input().split())
b = map(int, raw_input().split())
n = b[0]
final = b[1]
bag = []
j = 0
worth = 0
for i in range(n):
    if worth == final:
        print len(bag)
        exit()
    if raw_input() == 'Harry':
        bag.append(values[j])
        worth = worth + values[j]
        j = j + 1
    else:
        worth -= values[bag.pop()]
print len(bag)

