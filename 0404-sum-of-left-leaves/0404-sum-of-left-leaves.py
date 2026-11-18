# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: TreeNode | None) -> int:
        if not root:
            return 0
        queue=deque([(root,False)])
        tot=0
        while queue:
            node,isleft=queue.popleft()
            if isleft and not node.left and not node.right:
                tot+=node.val
            if node.left:
                queue.append((node.left,True))
            if node.right:
                queue.append((node.right,False))
        return tot                    
        