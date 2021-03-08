class Solution:
    def __init__(self):
        self.output = []
        
    def delNodes(self, root: TreeNode, to_delete: List[int]) -> List[TreeNode]:
        if root.val not in to_delete:
            self.output.append(root)
        queue = [root]
        while (queue):
            node = queue.pop(0)
            
            if node.val in to_delete:
                if node.left:
                    self.delNodes(node.left, to_delete)
                if node.right:
                    self.delNodes(node.right, to_delete)      
            else:
                if node.left:
                    queue.append(node.left)
                    if node.left.val in to_delete:
                        node.left = None

                if node.right:
                    queue.append(node.right)
                    if node.right.val in to_delete:
                        node.right = None

        return self.output