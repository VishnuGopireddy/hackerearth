'''
Python 2.7
Problem from Hackerearth on searching Breakup App
'''

lines = int(raw_input())
weight = [0,0]
for i in range(lines):
    line = str(raw_input())
    weight_19 = weight_21 = 0
    if line[0] == 'G':
        weight[0] = 2 * line.count('19') + weight[0]
        weight[1] = 2 * line.count('21') + weight[1]
    if line[0] == 'M':
        weight[0] = line.count('19') + weight[0]
        weight[1] = line.count('21') + weight[1]

if weight[0] > weight[1]:
    print 'Date'
else:print 'No Date'