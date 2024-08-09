from collections import deque

class Solution:
    def zigzagLevelOrder(self, root: TreeNode):
        if not root:
            return []

        result = []
        queue = deque([root])
        left_to_right = True

        while queue:
            level = deque()
            for _ in range(len(queue)):
                node = queue.popleft()
                if left_to_right:
                    level.append(node.val)
                else:
                    level.appendleft(node.val)

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            result.append(list(level))
            left_to_right = not left_to_right

        return result

# Example usage:
# root = TreeNode(3)
# root.left = TreeNode(9)
# root.right = TreeNode(20, TreeNode(15), TreeNode(7))
# sol = Solution()
# print(sol.zigzagLevelOrder(root))  # Output: [[3], [20, 9], [15, 7]]

class Solution:
    def buildTree(self, preorder: list[int], inorder: list[int]) -> TreeNode:
        if not preorder or not inorder:
            return None

        root_val = preorder.pop(0)
        root = TreeNode(root_val)
        inorder_index = inorder.index(root_val)

        root.left = self.buildTree(preorder, inorder[:inorder_index])
        root.right = self.buildTree(preorder, inorder[inorder_index + 1:])

        return root

# Example usage:
# preorder = [3, 9, 20, 15, 7]
# inorder = [9, 3, 15, 20, 7]
# sol = Solution()
# tree = sol.buildTree(preorder, inorder)
# # The constructed tree's structure can be tested with other traversal methods.