# -*- coding: utf-8 -*-
from xxlimited import Null


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


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


class Solution:
    def subtreeWithAllDeepest(self, root: TreeNode) -> TreeNode:
        current = 0
        left = self.get_depth(root.left, current + 1) if root.left else current
        right = self.get_depth(root.right, current + 1) if root.right else current
        print(f'node: {root.val}')
        print(f'left level: {left}')
        print(f'right level: {right}')
        if left == right:
            return root
        elif left > right:
            return self.subtreeWithAllDeepest(root.left)
        else:
            return self.subtreeWithAllDeepest(root.right)

    def get_depth(self, tree_node: TreeNode, deep):
        if tree_node.left is not None:
            left = self.get_depth(tree_node.left, deep + 1)
        else:
            left = deep
        if tree_node.right is not None:
            right = self.get_depth(tree_node.right, deep + 1)
        else:
            right = deep
        return max(left, right)


def main():
    nodes = [3, 5, 1, 6, 2, 0, 8, None, None, 7, 4]
    root = create_tree(nodes)
    # visit_node(root, 0)
    solution = Solution()
    sol = solution.subtreeWithAllDeepest(root)
    print(sol.val)


if __name__ == '__main__':
    main()

