# python 2.6
#Program on Memorise Me from HACKER EARTH

n = input()
inp = raw_input().split(' ')[:n]
print inp
freq = {}
for i in inp:
    if i not in freq:
        freq[i] = 1
    else:
        freq[i] += 1
q = input()
for i in range(q):
    j = raw_input()
    if j not in freq:
        print 'NOT PRESENT'
    else:
        print freq[j]