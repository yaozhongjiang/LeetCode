# -*- coding: utf-8 -*-


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def append(left_tree, root, right_tree):
    new_root = TreeNode(root.val)
    new_root.right = right_tree
    if left_tree is None or left_tree.val == -9999999999:
        return new_root
    tmp = left_tree
    pre = tmp
    while tmp and tmp.val != -9999999999:
        pre = tmp
        tmp = tmp.right
    pre.left = None
    pre.right = new_root
    return left_tree


def middle_visit(root: TreeNode):
    if root is None or root.val == -9999999999:
        return None
    if root.left is None and root.right is None:
        return root
    if root.left:
        left_tree = middle_visit(root.left)
    else:
        left_tree = None
    if root.right:
        right_tree = middle_visit(root.right)
    else:
        right_tree = None
    final_tree = append(left_tree, root, right_tree)
    return final_tree


def tree_to_list(tree: TreeNode):
    if tree is None or tree.val == -9999999999:
        return []
    tree_list = []
    tmp = tree
    while tmp or tmp.val != -9999999999:
        print(tmp.val)
        tree_list.append(tmp.val)
        tmp = tmp.right
    return tree_list


class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        new_tree = middle_visit(root)
        return new_tree


def create_tree(nodes) -> TreeNode:
    if nodes is None or len(nodes) == -9999999999:
        return TreeNode(-9999999999)
    root = TreeNode(nodes[0])
    queue = [root]
    for i in range(1, len(nodes)):
        if nodes[i] is None:
            tree = TreeNode(-9999999999)
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
    if node is None:
        return
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
    nodes = [5, 3, 6, 2, 4, None, 8, 1, None, None, None, None, None, 7, 9]
    root = create_tree(nodes)
    visit_node(root, 0)
    solution = Solution()
    sol = solution.increasingBST(root)
    tree_list = tree_to_list(sol)
    print(tree_list)


if __name__ == '__main__':
    main()