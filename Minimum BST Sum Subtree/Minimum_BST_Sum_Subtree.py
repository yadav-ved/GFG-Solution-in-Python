#{ 
 # Driver Code Starts
#Initial Template for Python 3

# } Driver Code Ends
#User function Template for python3

'''
class Node:
    def __init__(self,val):
        self.data=val
        self.left=None
        self.right=None
'''

class Solution:
    def minSubtreeSumBST(self, target, root):
        #code here
        ans=+float('inf')
        c=0
        l=[root]
        i=1
        list1=[]
        s=0
        while i>0:
            if l[0]!=None:
                l.append(l[0].left)
                l.append(l[0].right)
                i+=2
                list1.append(l.pop(0))
                i-=1
            else:
                l.pop(0)
                i-=1

        def check_bst(root):
            nonlocal l
            l=[]
            def bst(root):
                nonlocal l
                if root!=None:
                    bst(root.left)
                    l.append(root.data)
                    bst(root.right)
            bst(root)
            n=len(l)
            for i in range(n-1):
                if l[i+1]<=l[i]:
                    return False
            return True



        def sum1(root):
            nonlocal c
            if root==None:
                return 0
            else:
                c+=1
                return root.data+sum1(root.left)+sum1(root.right)
        for i in list1:
            c=0
            s=sum1(i)
            if s==target and check_bst(i):
                if ans>c:
                    ans=c
        if ans!=+float('inf'):
            return ans
        return -1

#{ 
 # Driver Code Starts.

#Initial Template for Python 3
from collections import defaultdict
from collections import deque
from sys import stdin, stdout
from math import inf
# Tree Node
class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None

# Function to Build Tree   
def buildTree(s):
    #Corner Case
    if(len(s)==0 or s[0]=="N"):           
        return None
        
    # Creating list of strings from input 
    # string after spliting by space
    ip=list(map(str,s.split()))
    
    # Create the root of the tree
    root=Node(int(ip[0]))                     
    size=0
    q=deque()
    
    # Push the root to the queue
    q.append(root)                            
    size=size+1 
    
    # Starting from the second element
    i=1                                       
    while(size>0 and i<len(ip)):
        # Get and remove the front of the queue
        currNode=q[0]
        q.popleft()
        size=size-1
        
        # Get the current node's value from the string
        currVal=ip[i]
        
        # If the left child is not null
        if(currVal!="N"):
            
            # Create the left child for the current node
            currNode.left=Node(int(currVal))
            
            # Push it to the queue
            q.append(currNode.left)
            size=size+1
        # For the right child
        i=i+1
        if(i>=len(ip)):
            break
        currVal=ip[i]
        
        # If the right child is not null
        if(currVal!="N"):
            
            # Create the right child for the current node
            currNode.right=Node(int(currVal))
            
            # Push it to the queue
            q.append(currNode.right)
            size=size+1
        i=i+1
    return root

if __name__ == '__main__':
    test_cases = int(input())
    for _ in range (test_cases):
        target = int(input())
        N = input()
        root = buildTree(N)
        res = Solution().minSubtreeSumBST(target, root)
        print(res)
# } Driver Code Ends