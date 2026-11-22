# Take the shortest string and grow its prefix one character at a time,
# checking every string with startswith; stop at the first prefix that fails.
# Time: O(n * m^2), Space: O(m)   (n = number of strings, m = length of the shortest)

class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        target = min(strs, key = len)
        m = len(target)
        cnt = ''
        for i in range(m):
            cnt = target[:i+1]
            if all(s.startswith(cnt) for s in strs):
                continue
            else:
                return cnt[:i]
        return target
