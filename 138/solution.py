"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        oldtonew = dict()
        cur = head
        newhead = None
        while(cur != None):
            if newhead == None:
                newhead = Node(cur.val)
                newcur = newhead
            else:
                temp = Node(cur.val)
                newcur.next = temp
                newcur = newcur.next
            oldtonew[cur] = newcur
            cur = cur.next
        cur = head
        newcur = newhead
        while(cur != None):
            if cur.random != None:
                newcur.random = oldtonew[cur.random]
            else:
                newcur.random = None
            newcur = newcur.next
            cur = cur.next
        return newhead
