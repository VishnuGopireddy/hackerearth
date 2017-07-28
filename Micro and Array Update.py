# python 2.6
#Program on Micro and Array Update from HACKER EARTH

n=input()
for i in range(0,n):
    n,k=map(int,raw_input().split())
    a=[]
    a=map(int,raw_input().split())
    x=min(a)
    if x<k:
        print k-x
    else:
        print "0"