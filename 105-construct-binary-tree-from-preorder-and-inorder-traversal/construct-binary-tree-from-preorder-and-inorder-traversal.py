class Solution:
    def buildTree(self, preorder, inorder):
        inorder_map = {}

        for i, value in enumerate(inorder):
            inorder_map[value] = i

        self.preorder_index = 0

        def dfs(left, right):
            if left > right:
                return None

            root_value = preorder[self.preorder_index]
            self.preorder_index += 1

            root = TreeNode(root_value)

            mid = inorder_map[root_value]

            root.left = dfs(left, mid - 1)
            root.right = dfs(mid + 1, right)

            return root

        return dfs(0, len(inorder) - 1)