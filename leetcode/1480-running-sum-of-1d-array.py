# Prefix sum
# Time: O(n), Space: O(1), best/worst case - identical
# input in-place modifies

class Solution:
    def runningSum(self, nums: list[int]) -> list[int]:
        for i in range(len(nums)-1):
            nums[i+1] = nums[i] + nums[i+1]
        return nums