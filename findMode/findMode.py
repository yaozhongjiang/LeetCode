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
        return list


def main():
    root = TreeNode()
    solution = Solution()
    sol = solution.findMode(root)
    print(sol)


if __name__ == '__main__':
    main()