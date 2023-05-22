# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return root
        cnt = 0
        array = [[root], []]
        ans = [[root.val]]
        while len(array[cnt%2]) != 0:
            temp = []
            for i in array[cnt%2]:
                if i.left and not cnt%2:
                    temp.append(i.left.val)
                    array[(cnt+1)%2].append(i.left)
                if i.right:
                    temp.append(i.right.val)
                    array[(cnt+1)%2].append(i.right)
                if i.left and cnt%2:
                    temp.append(i.left.val)
                    array[(cnt+1)%2].append(i.left)
            array[(cnt+1)%2] = array[(cnt+1)%2][::-1]
            temp = temp[::-1]
            array[cnt%2] = []
            if temp:
                ans.append(temp)
            cnt+=1
        return ans
