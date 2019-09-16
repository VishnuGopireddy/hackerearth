#https://www.hackerearth.com/practice/data-structures/linked-list/singly-linked-list/practice-problems/algorithm/remove-friends-5/

class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
class singly:
    def __init__(self):
        self.head = None
    def insert(self,data):
        new_node = Node(data)
        if self.head == None:
            self.head = new_node
        else:
            curr = self.head
            while curr.next != None:
                curr = curr.next
            curr.next = new_node
    def print_list(self):
        if self.head == None:
            print('list is empty')
        else:
            curr = self.head
            while curr != None:
                print(curr.data,end=' ')
                curr = curr.next

    def detete(self,item):
        '''
        Deletes a particular datanode
        :param item: Item ehich has to be deleted
        :return: True if delete else false
        '''
        if self.head == None:
            print('Cann\'t delete')
            return False
        elif self.head.data == item:
            curr = self.head
            self.head = self.head.next
            del(curr)
            return True
        else:
            curr = self.head
            prev = curr
            while curr.data != item:
                prev = curr
                curr = curr.next
            prev.next = curr.next
            return True

    def get_ith(self,i):
        '''
        Return ith item and i +1 th item from list
        :param i: index
        :return: ith and i+1th item
        '''
        if self.head == None:
            return None
        else:
            pass


'''s = singly()
s.insert(10)
s.insert(15)
s.insert(20)
s.insert(25)
s.print_list()
s.detete(25)
s.insert(38)
s.print_list()'''

kases = int(input())
for kase in kases:
    n,k = map(int,input().split())
    arr = map(int,input().split())
    friends = singly()
    for i in arr:
        friends.insert(i)
    while k > 0:
        delete_friend = False
        for i in range(n-1-k):
            if arr[i] < arr[i+1]:
                friends.detete(3)
                arr.pop(i)
                k = k -1
                delete_friend = True
        if delete_friend == False:
            friends.detete(arr[n+k])

    friends.print_list()