# if num count > 2
# Time: O(n); Space: O(n)
# Worst case - not duplicate, all cycle
# Best case - duplicate in (0, 1) elements

class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        dict_count_elem = {}
        for i in range (len(nums)):
            if nums[i] in dict_count_elem:
                return True
            else:
                dict_count_elem[nums[i]] = i
        return False
