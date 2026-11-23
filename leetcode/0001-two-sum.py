# store each seen value with its index; for each x check whether target - x was already seen.
# Time: O(n), Space: O(n)

class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        dict_of_nums = {}
        for i in range(len(nums)):
            first_ind = target - nums[i]
            if (first_ind) in dict_of_nums:
                return [dict_of_nums[first_ind], i]
            else:
                dict_of_nums[nums[i]] = i   
