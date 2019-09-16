'''
Python 2.7
Problem from Hackerearth on searching Monk Takes a Walk
'''

kases = int(raw_input())
vowels = ['A' 'E' 'I' 'O' 'U' 'a' 'e' 'i' 'o' 'u']
for i in range(kases):
    characters_of_trees = str(raw_input())
    count_vowels = 0
    for j in characters_of_trees:
        if j == 'A' or j == 'E' or j == 'I' or j == 'O' or j == 'U' or j == 'a' or j =='e' or j == 'i' or j == 'o' or j == 'u':
            count_vowels += 1
    print count_vowels

