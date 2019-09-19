'''
Python 2.7
Problem from Hackerearth on Manna's First Name
'''
no_of_words = int(raw_input())
for i in range(no_of_words):
    word = raw_input()
    SUVO = word.count('SUVO')
    SUVOJIT = word.count('SUVOJIT')
    print 'SUVO = %d, SUVOJIT = %d ' % (SUVO - SUVOJIT, SUVOJIT)
