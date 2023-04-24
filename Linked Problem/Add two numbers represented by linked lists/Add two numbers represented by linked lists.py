#User function Template for python3

''' Node for linked list:

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

'''
class Solution:
    #Function to add two numbers represented by linked list.
    def addTwoLists(self, first, second):
        # code here
        # return head of sum list
        tempf = first
        fs = 0
        ss = 0
        c1 = 0
        c2 = 0
        while tempf:
            fs =(fs*10)+tempf.data
            c1 += 1
            tempf = tempf.next
        temps = second
        while temps:
            ss =(ss*10)+temps.data
            c2 += 1
            temps=temps.next
            
        s = fs+ss
        s =str(s)
        s = list(map(int,s))
        head = None
        def insert(self,val):
            new = Node(vol)
            if self.head is None:
                self.head=new
            else:
                temp=self.head
                while temp:
                    temp.data=new
                    temp=temp.next
        L3=LinkedList()
        for i in s:
            L3.insert(i)
        return L3.head


#{ 
 # Driver Code Starts
#Initial Template for Python 3

# Node Class
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# Linked List Class
class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    # creates a new node with given value and appends it at the end of the linked list
    def insert(self, val):
        if self.head is None:
            self.head = Node(val)
            self.tail = self.head
        else:
            self.tail.next = Node(val)
            self.tail = self.tail.next

# prints the elements of linked list starting with head
def printList(n):
    while n:
        print(n.data,end=' ')
        n = n.next
    print()

if __name__ == '__main__':
    for _ in range(int(input())):
        
        n = int(input())
        arr1 = ( int(x) for x in input().split() )
        LL1 = LinkedList()
        for i in arr1:
            LL1.insert(i)
        
        m = int(input())
        arr2 = ( int(x) for x in input().split() )
        LL2 = LinkedList()
        for i in arr2:
            LL2.insert(i)
        
        res = Solution().addTwoLists(LL1.head, LL2.head)
        printList(res)
# } Driver Code Ends