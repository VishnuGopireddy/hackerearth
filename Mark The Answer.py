# python 2.6
#Program on Mark The Answer from HACKER EARTH

b = raw_input().split()
n = int(b[0])
x = int(b[1])
diff = map(int, raw_input().split())
count = 0
skip = 0
for i in range(n):
    if diff[i] <= x:
        count +=1
    elif diff[i]>x and skip == 0:
        skip = 1
    elif diff[i]>x:
        break
print count
