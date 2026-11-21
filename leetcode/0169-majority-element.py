# Boyer-Moore majority vote: keep a candidate and a counter; an equal element
# increments the counter, a different one decrements it, at zero the candidate is replaced.
# Time: O(n), Space: O(1)

# Hash map count: Time O(n), Space O(n)
# class Solution:
#     def majorityElement(self, nums: list[int]) -> int:
#         dict_n = {}
#         for i in nums:
#             if i in dict_n:
#                 dict_n[i] += 1
#             else:
#                 dict_n[i] = 1
#         return max(dict_n, key = dict_n.get)


class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        cand = 0
        count = 0
        for n in nums:
            if count == 0:
                cand = n
                count = 1
            elif n == cand:
                count += 1
            else:
                count -= 1
        return cand
