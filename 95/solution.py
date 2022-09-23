# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        def dfs(nums):
            if not nums:
                return [None]
            
            ans = []
            for i in range(len(nums)):
                leftTrees = dfs(nums[:i]) # a list of all possible left trees
                rightTrees = dfs(nums[i+1:]) # a list of all possible right trees
                
                for l in leftTrees: # traverse the list of left trees
                    for r in rightTrees: # traverse the list of right trees
                        root = TreeNode(nums[i])
                        root.left = l
                        root.right = r
                        ans.append(root)
            return ans
            
        nums = list(range(1, n+1))
        return dfs(nums)
