'''
# node class:

class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None

'''

class Solution:
    def ladoos(self, root, home, k):
        # Your code goes here
        pMap = {}
        self.fillParentMap(pMap, None, root)
        targetNode = self.searchNode(root, home)
        return self.bfsTraversal(set(), pMap, targetNode, k)

    def fillParentMap(self, pMap, parent, root):
        if root is None:
            return
        pMap[root] = parent
        self.fillParentMap(pMap, root, root.left)
        self.fillParentMap(pMap, root, root.right)

    def searchNode(self, root, target):
        if root is None or root.data == target:
            return root
        left = self.searchNode(root.left, target)
        if left is not None:
            return left
        return self.searchNode(root.right, target)

    def bfsTraversal(self, vis, pMap, root, k):
        sum = 0
        q = []
        q.append(root)
        vis.add(root)

        while len(q) > 0 and k >= 0:
            size = len(q)

            while size > 0:
                curr = q.pop(0)

                par = pMap.get(curr)
                left = curr.left
                right = curr.right

                sum += curr.data
                if par is not None and par not in vis:
                    vis.add(par)
                    q.append(par)

                if left is not None and left not in vis:
                    vis.add(left)
                    q.append(left)

                if right is not None and right not in vis:
                    vis.add(right)
                    q.append(right)

                size -= 1

            k -= 1

        return sum