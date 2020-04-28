# -*- coding: utf-8 -*-

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        node = TreeNode()
        return node


def create_tree(nodes) -> TreeNode:
    root = TreeNode(nodes[0])
    queue = [root]
    for i in range(1, len(nodes)):
        if nodes[i] is None:
            tree = None
        else:
            tree = TreeNode(nodes[i])
        if i % 2 == 1:
            node = queue.pop(0)
        if i % 2 == 1:
            node.left = tree
        else:
            node.right = tree
        queue.append(tree)
    return root


def visit_node(node: TreeNode, depth):
    print(f'{node.val} ---> {depth}')
    if node.left:
        visit_node(node.left, depth + 1)
    else:
        print(f'left leaf ---> {depth}')
    if node.right:
        visit_node(node.right, depth + 1)
    else:
        print(f'right leaf ---> {depth}')


def main():
    nodes = [3, 5, 1, 6, 2, 0, 8, None, None, 7, 4]
    root = create_tree(nodes)
    # visit_node(root, 0)
    solution = Solution()
    sol = solution.subtreeWithAllDeepest(root)
    print(sol.val)


if __name__ == '__main__':
    main()