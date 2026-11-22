# Put all values into a set, then collect every number from 1..n
# that is not in it.
# Time: O(n), Space: O(n)

class Solution:
    def findDisappearedNumbers(self, nums: list[int]) -> list[int]:
        n = len(nums)
        seen = set(nums)
        result = []
        for i in range(1, n + 1):
            if i not in seen:
                result.append(i)
        return result
