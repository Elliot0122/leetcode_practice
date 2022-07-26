"""
# Definition for a Node.
class Node(object):
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution(object):
    def cloneGraph(self, node):
        """
        :type node: Node
        :rtype: Node
        """
        node_copy = self.dfs(node, dict())
        return node_copy
    
    def dfs(self, node, dic):
        if not node: return None
        if node in dic: return dic[node]
        node_cp = Node(node.val, [])
        dic[node] = node_cp
        for n in node.neighbors:
            neighbors_cp = self.dfs(n, dic)
            if neighbors_cp:
                node_cp.neighbors.append(neighbors_cp)
        return node_cp
        
