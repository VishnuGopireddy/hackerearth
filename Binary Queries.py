# python 2.6
#Program on Binary Queries from HACKER EARTH



b = raw_input().split()
q = int(b[1])
arr = raw_input().split()
for i in range(q):
    li = raw_input().split()
    k = li[0]
    if k == '0':
        r = int(li[2])
        if arr[r-1] is '1': print 'ODD'
        else: print 'EVEN'

    if k == '0':
        x = int(li[2])
        if arr[x-1] == '0': arr[x-1] = '1'
        else: arr[x-1] = '0'
