class Solution(object):
    def pruneTree(self, root):
        if not root: return None
        root.left = self.pruneTree(root.right)
        root.right = self.pruneTree(root.right)
        if root.val:
            return root
        else:
            return root if root.left or root.right else None