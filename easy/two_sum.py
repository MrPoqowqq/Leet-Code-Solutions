from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        all_nums = {}
        for i, v in enumerate(nums):
            complement = target - v
            if complement in all_nums:
                return [i, all_nums[complement]]
            else:
                all_nums[v] = i


if __name__ == "__main__":
    nums = [2, 7, 11, 15]
    target = 9

    sol = Solution()
    result = sol.twoSum(nums, target)

    print(f"Input: nums = {nums}, target = {target}")
    print(f"Output: {result}")
