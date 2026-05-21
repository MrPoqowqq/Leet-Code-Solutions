from typing import List


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        k = 0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[k] = nums[i]
                k += 1
        return k


if __name__ == "__main__":
    sol = Solution()

    test_nums = [3, 2, 2, 3]
    test_val = 3

    print(f"Original array: {test_nums}, remove {test_val}")
    k = sol.removeElement(test_nums, test_val)

    print(f"Returned : {k}")
    print(f"Modified array (first k elements): {test_nums[:k]}")
