# Compare characters column by column against the shortest string and stop at
# the first mismatch; the answer is the shortest string's prefix before it.
# Time: O(n * m), Space: O(1) extra   (n = number of strings, m = length of the shortest)

# startswith version: Time O(n * m^2), Space O(m)
# class Solution:
#     def longestCommonPrefix(self, strs: list[str]) -> str:
#         target = min(strs, key = len)
#         m = len(target)
#         cnt = ''
#         for i in range(m):
#             cnt = target[:i+1]
#             if all(s.startswith(cnt) for s in strs):
#                 continue
#             else:
#                 return cnt[:i]
#         return target


class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        target = min(strs, key = len)
        m = len(target)
        for i in range(m):
            if all(s[i] == target[i] for s in strs):
                continue
            else:
                return target[:i]
        return target
