# -*- coding: utf-8 -*-
import copy
from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> List[List[int]]:
        if root is None:
            return []
        if root.left is None and root.right is None:
            if root.val == sum:
                return [[root.val]]
            else:
                return []
        list_sum = sum
        list_depth = [root.val]
        final = []
        if root.left is not None:
            self.visit_depth(root.left, list_sum, list_depth, final)
        if root.right is not None:
            self.visit_depth(root.right, list_sum, list_depth, final)
        return final

    def visit_depth(self, left: TreeNode, list_sum, list_depth, final):
        if left.left is None and left.right is None:
            list_depth.append(left.val)
            if sum(list_depth) == list_sum:
                final.append(copy.deepcopy(list_depth))
            list_depth.pop(-1)

        if left.left is not None:
            list_depth.append(left.val)
            self.visit_depth(left.left, list_sum, list_depth, final)
            list_depth.pop(-1)
        if left.right is not None:
            list_depth.append( left.val )
            self.visit_depth(left.right, list_sum, list_depth, final)
            list_depth.pop(-1)


def create_tree(nodes) -> TreeNode:
    if nodes is None or len(nodes) == 0:
        return TreeNode(0)
    root = TreeNode(nodes[0])
    queue = [root]
    for i in range(1, len(nodes)):
        if nodes[i] is None:
            tree = TreeNode(0)
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
    # nodes = [5, 4, 8, 11, None, 13, 4, 7, 2, None, None, None, None, 5, 1]
    # sum = 22
    # nodes = []
    # sum = 1
    nodes = [1, 2]
    sum = 0
    root = create_tree(nodes)
    # visit_node(root, 0)
    solution = Solution()
    sol = solution.pathSum(root, sum)
    print(sol)


if __name__ == '__main__':
    main()

