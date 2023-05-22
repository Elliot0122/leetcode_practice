"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if not root:
            return root
        cnt = 0
        array = [[root], []]
        ans = [[root.val]]
        while len(array[cnt%2]) != 0:
            for i in range(len(array[cnt%2])-1):
                array[cnt%2][i].next = array[cnt%2][i+1]
            for i in array[cnt%2]:
                if i.left:
                    array[(cnt+1)%2].append(i.left)
                if i.right:
                    array[(cnt+1)%2].append(i.right)
            array[cnt%2] = []
            cnt+=1
        return root
