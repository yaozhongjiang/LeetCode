# -*- coding: utf-8 -*-
from typing import List


class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        for i in range(len(nums)):
            for j in range(len(nums)):
                if nums[i] < nums[j]:
                    temp = nums[i]
                    nums[i] = nums[j]
                    nums[j] = temp
        print(nums)


def main():
    nums = [2,0,2,1,1,0]
    solution = Solution()
    solution.sortColors(nums)


if __name__ == '__main__':
    main()

