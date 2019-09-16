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
            del(curr)
            return True

    def friend_delete(self,k):
        while k > 0:
            is_delete = False
            curr = self.head
            while curr.next.next != None:
                if curr.data < curr.next.data:
                    self.detete(curr.data)
                    is_delete = True
                    k = k-1
                    break
                curr = curr.next
            if is_delete == False:
                self.delete_last()
                k = k-1
            print('k =',k)
    def delete_last(self):
        if self.head == None:
            return
        elif self.head.next == None:
            self.head = None
        else:
            curr =self.head
            prev = curr
            while curr.next != None:
                curr = curr.next
                prev = curr
            prev.next = curr.next
            del(prev)
'''s = singly()
s.insert(10)
s.insert(15)
s.insert(20)
s.insert(25)
s.print_list()
s.detete(25)
s.insert(38)
s.print_list()
'''
n,k = map(int,input().split())
arr = list(map(int,input().split()))
friends = singly()
for i in arr:
    friends.insert(i)

friends.friend_delete(k)
friends.print_list()
