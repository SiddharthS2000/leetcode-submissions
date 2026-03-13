# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution(object):
    def minDepth(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        depth = 1
        if not root:
            return 0

        q = deque([root])

        while q:
            for i in range(0, len(q)):
                node = q.popleft()
                if not node.left and not node.right:
                    return depth

                if node.left:
                    q.append(node.left)
                
                if node.right:
                    q.append(node.right)
            depth += 1
        
        return depth
        
