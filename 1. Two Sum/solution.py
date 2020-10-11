from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dict_ = {}
        i = 0
        while i < len(nums):
            diff = target - nums[i]
            if diff in dict_:
                return [dict_[diff], i]

            dict_[nums[i]] = i
            i += 1
