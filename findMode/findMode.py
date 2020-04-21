# -*- coding: utf-8 -*-
from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def findMode(self, root: TreeNode) -> List[int]:
        list = []
        dics = {}
        self.statistic(root, dics)
        if len(dics) == 0:
            return []
        dics = sorted( dics.items(), key=lambda kv: (kv[1], kv[0]), reverse=True)
        count = 0
        for i in dics:
            if i[1] >= count:
                list.append(i[0])
                count = i[1]
        return list

    def statistic(self, tree_node: TreeNode, static_map):
        if tree_node is None:
            return {}
        if tree_node.val in static_map:
            static_map[tree_node.val] += 1
        else:
            static_map[tree_node.val] = 1
        if tree_node.left:
            self.statistic(tree_node.left, static_map)
        if tree_node.right:
            self.statistic(tree_node.right, static_map)


def create_tree(nodes) -> TreeNode:
    if len(nodes) == 0:
        return None
    root = TreeNode(nodes[0])
    queue = [root]
    for i in range(1, len(nodes)):
        node = queue.pop(0)
        if node is None:
            continue
        else:
            if nodes[i] is None:
                tree = None
            else:
                tree = TreeNode(nodes[i])
            node.left = tree
            queue.append( tree )
            i += 1
            if i < len(nodes):
                if nodes[i] is None:
                    tree = None
                else:
                    tree = TreeNode(nodes[i])
                node.right = tree
                queue.append(tree)
    return root


def visit_node(node: TreeNode, depth):
    if node is None:
        return None
    print(f'{node.val} ---> {depth}')
    if node.left:
        visit_node(node.left, depth + 1)
    else:
        print(f'left leaf ---> {depth + 1}')
    if node.right:
        visit_node(node.right, depth + 1)
    else:
        print(f'right leaf ---> {depth + 1}')


def main():
    nodes = []
    root = create_tree(nodes)
    visit_node(root, 0)
    solution = Solution()
    sol = solution.findMode(root)
    print(sol)


if __name__ == '__main__':
    main()