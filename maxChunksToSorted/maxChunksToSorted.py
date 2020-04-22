# -*- coding: utf-8 -*-
from typing import List


class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        if arr is None or len(arr) <= 0:
            return 0
        if len(arr) <= 1:
            return 1
        chunk = self.split_chunk(arr)
        return chunk

    def split_chunk(self, arr):
        if arr is None or len(arr) <= 0:
            return 0
        if len(arr) == 1:
            return 1
        if max(arr) == min(arr):
            return len(arr)
        for i in range(len(arr) - 1):
            arr_left = arr[:i + 1]
            arr_right = arr[i + 1:]
            max_left = max(arr_left)
            min_right = min(arr_right)
            if max_left <= min_right:
                break
            if i == len(arr) - 2:
                return 1

        return self.split_chunk(arr_left) + self.split_chunk(arr_right)


def main():
    # arr = [5,4,3,2,1]
    # arr = [2,1,3,4,4]
    # arr = [1,0,1,3,2]
    # arr = [1,1,0,0,1]
    # arr = [0,0,1,1,1]
    # arr = [2,1,3,4,4]
    # arr = [4,0,0,2,4]
    arr = [0,0,1,1,0,1,1,1,1,0]
    solution = Solution()
    sol = solution.maxChunksToSorted(arr)
    print(sol)


if __name__ == '__main__':
    main()

