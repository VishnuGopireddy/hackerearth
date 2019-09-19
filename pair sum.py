#https://www.hackerearth.com/practice/data-structures/hash-tables/basics-of-hash-tables/practice-problems/algorithm/pair-sums/

#python 3.6

n,k = 5,9
arr = [5,1,2,3,4]

#n,k = map(int,input().split())
#arr = list(map(int,input().split()))
sum = 0
i =  0
j = n-1
while i < j and arr[i] + arr[j] != k:
    if arr[i] + arr[j] > k:
        j = j -1
    elif arr[i] + arr[j] < k:
        i = i + 1

if arr[i] + arr[j] == k:
    print('YES')

