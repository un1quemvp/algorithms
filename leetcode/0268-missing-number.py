# Expected sum of 0..n (n * (n + 1) // 2) minus the actual sum of nums
# gives the missing number.
# Time: O(n), Space: O(1)

class Solution:
    def missingNumber(self, nums: list[int]) -> int:
        n = len(nums)
        max_sum = n * (n + 1) // 2
        n_sum = sum(nums)
        return max_sum - n_sum
