# Build a set from each array and return their intersection;
# set lookups are O(1) on average, so there are no nested scans.
# Time: O(n + m), Space: O(n + m)

# Brute force with list scans: Time O(n * m), Space O(min(n, m))
# class Solution:
#     def intersection(self, nums1: list[int], nums2: list[int]) -> list[int]:
#         insec = []
#         for i in nums1:
#             if i in nums2 and i not in insec:
#                 insec.append(i)
#         return insec


class Solution:
    def intersection(self, nums1: list[int], nums2: list[int]) -> list[int]:
        insec_1 = set(nums1)
        insec_2 = set(nums2)
        return list(insec_1 & insec_2)
