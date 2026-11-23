# keep a set of seen values; return True on the first repeat.
# Time: O(n), Space: O(n)

class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        dict_count_elem = {}
        for i in range (len(nums)):
            if nums[i] in dict_count_elem:
                return True
            else:
                dict_count_elem[nums[i]] = i
        return False
