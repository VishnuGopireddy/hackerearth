# python 2.6
#Program on Monk and Power of Time from HACKER EARTH

n = int(raw_input())
Calling_Order = map(int, raw_input().split())
Ideal_Order = map(int, raw_input().split())
Time = 0

while Calling_Order:
    if Calling_Order[0] == Ideal_Order[0]:
        Calling_Order.pop(0)
        Ideal_Order.pop(0)
        Time += 1
    else:
        Calling_Order.append(Calling_Order.pop(0))
        Time += 1

print Time